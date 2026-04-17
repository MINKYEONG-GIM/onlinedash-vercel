from __future__ import annotations

import streamlit as st

from app.config import AppConfig
from app.constants import BRAND_KEY_TO_SHEET_NAME
from app.services.google_sheets import fetch_sheet_bytes


@st.cache_data(ttl=300)
def get_all_sources(cfg: AppConfig) -> dict[str, tuple[bytes | None, str]]:
    out: dict[str, tuple[bytes | None, str]] = {"inout": (fetch_sheet_bytes(cfg.base_spreadsheet_id), "inout")}
    online_bytes = fetch_sheet_bytes(cfg.online_spreadsheet_id) if cfg.online_spreadsheet_id else None
    for brand_key in BRAND_KEY_TO_SHEET_NAME:
        out[brand_key] = (online_bytes, brand_key)
    return out

