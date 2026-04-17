from __future__ import annotations


GOOGLE_SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]


BRAND_KEY_TO_SHEET_NAME = {
    "spao": "스파오",
    "whoau": "후아유",
    "clavis": "클라비스",
    "mixxo": "미쏘",
    "roem": "로엠",
    "shoopen": "슈펜",
    "eblin": "에블린",
    "newbalance": "뉴발란스",
    "nbkids": "뉴발란스키즈",
}

BRAND_TO_KEY = {
    "스파오": "spao",
    "후아유": "whoau",
    "클라비스": "clavis",
    "미쏘": "mixxo",
    "로엠": "roem",
    "슈펜": "shoopen",
    "에블린": "eblin",
    "뉴발란스": "newbalance",
    "뉴발란스키즈": "nbkids",
}


BRANDS_DEFAULT_LIST = [
    "스파오",
    "뉴발란스",
    "뉴발란스키즈",
    "후아유",
    "슈펜",
    "미쏘",
    "로엠",
    "클라비스",
    "에블린",
]

BU_GROUPS = [
    ("캐쥬얼BU", ["스파오"]),
    ("스포츠BU", ["뉴발란스", "뉴발란스키즈", "후아유", "슈펜"]),
    ("여성BU", ["미쏘", "로엠", "클라비스", "에블린"]),
]


NO_REG_SHEET_BRANDS: set[str] = set()

