"""Chuẩn bị tập phân tích riêng cho Giả thuyết 3 sau FR04."""

from collections.abc import Iterable

import numpy as np
import pandas as pd

from .config import (
    ANALYSIS_CUTOFF_DATE,
    OFFPEAK_LABEL,
    PEAK_LABEL,
    PEAK_MONTHS,
)


REQUIRED_COLUMNS = {
    "id",
    "status",
    "release_date",
    "release_year",
    "release_month",
    "revenue",
}


def require_columns(
    data: pd.DataFrame,
    required_columns: Iterable[str] = REQUIRED_COLUMNS,
) -> None:
    """Báo lỗi rõ ràng nếu dữ liệu sau FR04 thiếu cột cần thiết."""
    missing_columns = set(required_columns) - set(data.columns)
    if missing_columns:
        missing_text = ", ".join(sorted(missing_columns))
        raise KeyError(f"H3 thiếu cột bắt buộc: {missing_text}")


def validate_fr04_input(data: pd.DataFrame) -> dict[str, bool]:
    """Kiểm tra các cam kết đầu vào đã được FR04 xử lý."""
    require_columns(data)

    checks = {
        "ID đã duy nhất sau FR04": bool(data["id"].is_unique),
        "Ngày phát hành không còn thiếu": bool(
            data["release_date"].notna().all()
        ),
        "Tháng phát hành nằm trong khoảng 1-12": bool(
            data["release_month"].between(1, 12).all()
        ),
        "Năm phát hành không còn thiếu": bool(
            data["release_year"].notna().all()
        ),
    }

    failed_checks = [
        name
        for name, passed in checks.items()
        if not passed
    ]
    if failed_checks:
        failed_text = "; ".join(failed_checks)
        raise ValueError(
            "Dữ liệu đầu vào chưa thỏa điều kiện FR04: "
            f"{failed_text}"
        )

    return checks


def prepare_hypothesis_3_data(
    clean_data: pd.DataFrame,
    *,
    cutoff_date: str | pd.Timestamp = ANALYSIS_CUTOFF_DATE,
    peak_months: Iterable[int] = PEAK_MONTHS,
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, bool]]:
    """Lọc tập H3 và tạo các cột phân tích riêng của giả thuyết."""
    checks = validate_fr04_input(clean_data)
    cutoff_timestamp = pd.Timestamp(cutoff_date)
    peak_month_set = set(peak_months)

    hypothesis_data = clean_data.loc[
        clean_data["status"].eq("Released")
        & clean_data["release_date"].le(cutoff_timestamp)
        & clean_data["revenue"].gt(0)
    ].copy()

    # ID đã được xử lý ở FR04. H3 chỉ xác nhận, không xóa trùng lần nữa.
    if not hypothesis_data["id"].is_unique:
        raise ValueError(
            "Tập H3 vẫn còn ID lặp dù FR04 phải bảo đảm ID duy nhất."
        )

    hypothesis_data["release_decade"] = (
        hypothesis_data["release_year"] // 10
    ) * 10
    hypothesis_data["season_group"] = np.where(
        hypothesis_data["release_month"].isin(peak_month_set),
        PEAK_LABEL,
        OFFPEAK_LABEL,
    )

    quality_trace = pd.DataFrame(
        [
            {
                "giai_doan": "Dữ liệu sạch chung sau FR04",
                "so_dong": len(clean_data),
            },
            {
                "giai_doan": (
                    "Tập H3: đã phát hành, trước ngày chốt, "
                    "doanh thu lớn hơn 0"
                ),
                "so_dong": len(hypothesis_data),
            },
        ]
    )

    return hypothesis_data, quality_trace, checks
