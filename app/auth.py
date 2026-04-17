from __future__ import annotations

import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

from app.config import AppConfig


def make_cookie_manager(cfg: AppConfig) -> EncryptedCookieManager:
    password = cfg.cookie_password or "change-me"
    return EncryptedCookieManager(prefix="style_dashboard", password=password)


def require_auth(cfg: AppConfig, cookies: EncryptedCookieManager) -> None:
    if not cookies.ready():
        st.stop()

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    expected = (cfg.dashboard_password or "").strip()
    if not expected:
        st.session_state.authenticated = True
        return

    if cookies.get("logged_in") == "true":
        st.session_state.authenticated = True
        return

    if st.session_state.authenticated:
        return

    st.markdown(
        "<div style='max-width:400px;margin:4rem auto;padding:2rem;"
        "background:#1e293b;border-radius:12px;border:1px solid #334155;'>",
        unsafe_allow_html=True,
    )
    st.markdown("### 🔐 비밀번호를 입력하세요")

    pw = st.text_input(
        "비밀번호",
        type="password",
        key="auth_password",
        placeholder="비밀번호 입력",
    )

    if st.button("입장", key="auth_submit"):
        if pw.strip() == expected:
            st.session_state.authenticated = True
            cookies["logged_in"] = "true"
            cookies.save()
            st.rerun()
        else:
            st.error("비밀번호가 올바르지 않습니다")

    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

