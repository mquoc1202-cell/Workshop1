"""Các quy tắc được xác định trước cho Giả thuyết 3."""

import pandas as pd


PEAK_MONTHS = frozenset({5, 6, 7, 11, 12})
ANALYSIS_CUTOFF_DATE = pd.Timestamp("2026-09-23")
MINIMUM_GROUP_SIZE = 30
REQUIRED_UPLIFT_PERCENT = 40.0

OFFPEAK_LABEL = "Thấp điểm"
PEAK_LABEL = "Cao điểm"
SEASON_ORDER = (OFFPEAK_LABEL, PEAK_LABEL)
