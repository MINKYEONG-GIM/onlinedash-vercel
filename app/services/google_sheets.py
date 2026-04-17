from __future__ import annotations

import json
import os
from io import BytesIO
from pathlib import Path

import streamlit as st
from google.oauth2.service_account import Credentials

from app.constants import GOOGLE_SCOPES


def _base_dir() -> str:
    return str(Path(__file__).resolve().parents[2])


def _get_google_credentials() -> Credentials | None:
    try:
        raw = getattr(st.secrets, "get", lambda k, d=None: None)("google_service_account") or st.secrets.get(
            "google_service_account", None
        )
        if raw:
            info = json.loads(raw) if isinstance(raw, str) else dict(raw)
            if "type" in info and "private_key" in info:
                return Credentials.from_service_account_info(info, scopes=GOOGLE_SCOPES)
    except Exception:
        pass

    creds_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not creds_path or not os.path.isfile(creds_path):
        base_dir = _base_dir()
        for name in ("service_account.json", "credentials.json"):
            p = os.path.join(base_dir, name)
            if os.path.isfile(p):
                creds_path = p
                break
    if not creds_path:
        return None

    try:
        return Credentials.from_service_account_file(creds_path, scopes=GOOGLE_SCOPES)
    except Exception:
        return None


def _fetch_sheet_via_api(sheet_id: str, creds: Credentials) -> bytes | None:
    try:
        from googleapiclient.discovery import build
        from openpyxl import Workbook

        svc = build("sheets", "v4", credentials=creds, cache_discovery=False)
        meta = svc.spreadsheets().get(spreadsheetId=sheet_id).execute()
        names = [s["properties"]["title"] for s in meta.get("sheets", [])]
        if not names:
            return None

        wb = Workbook()
        wb.remove(wb.active)

        for idx, title in enumerate(names):
            try:
                rng = f"'{title.replace(chr(39), chr(39) * 2)}'" if title else f"Sheet{idx + 1}"
                rows = (
                    svc.spreadsheets()
                    .values()
                    .get(spreadsheetId=sheet_id, range=rng)
                    .execute()
                    .get("values", [])
                )
            except Exception:
                rows = []

            ws = wb.create_sheet(title=(title[:31] if title else f"Sheet{idx + 1}"), index=idx)
            for row in rows:
                ws.append(row)

        out = BytesIO()
        wb.save(out)
        out.seek(0)
        return out.read()
    except Exception:
        return None


@st.cache_data(ttl=300)
def fetch_sheet_bytes(sheet_id: str) -> bytes | None:
    if not sheet_id:
        return None

    creds = _get_google_credentials()
    if not creds:
        return None

    try:
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaIoBaseDownload

        service = build("drive", "v3", credentials=creds, cache_discovery=False)
        fh = BytesIO()
        downloader = MediaIoBaseDownload(
            fh,
            service.files().export_media(
                fileId=sheet_id,
                mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            ),
        )
        while True:
            _, done = downloader.next_chunk()
            if done:
                break
        fh.seek(0)
        return fh.read()
    except Exception:
        pass

    return _fetch_sheet_via_api(sheet_id, creds)

