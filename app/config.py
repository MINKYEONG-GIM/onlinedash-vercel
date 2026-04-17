from __future__ import annotations

import os
from dataclasses import dataclass

import streamlit as st


def _secret(key: str, default: str = "") -> str:
    try:
        v = st.secrets.get(key, default) or default
        return str(v).strip() if v else default
    except Exception:
        return default


@dataclass(frozen=True)
class AppConfig:
    dashboard_password: str
    cookie_password: str

    base_spreadsheet_id: str
    online_spreadsheet_id: str


def load_config() -> AppConfig:
    dashboard_password = _secret("DASHBOARD_PASSWORD") or os.environ.get("DASHBOARD_PASSWORD", "").strip()
    cookie_password = _secret("COOKIE_PASSWORD") or os.environ.get("COOKIE_PASSWORD", "").strip()

    base_spreadsheet_id = str(_secret("BASE_SPREADSHEET_ID")).strip() or ""
    online_spreadsheet_id = str(_secret("ONLINE_SPREADSHEET_ID")).strip() or ""

    return AppConfig(
        dashboard_password=dashboard_password,
        cookie_password=cookie_password,
        base_spreadsheet_id=base_spreadsheet_id,
        online_spreadsheet_id=online_spreadsheet_id,
    )

