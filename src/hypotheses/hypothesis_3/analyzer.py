"""Các phép tính phân tích cho Giả thuyết 3."""

import numpy as np
import pandas as pd

from .config import (
    MINIMUM_GROUP_SIZE,
    OFFPEAK_LABEL,
    PEAK_LABEL,
    REQUIRED_UPLIFT_PERCENT,
    SEASON_ORDER,
)


def calculate_uplift_percent(
    baseline_value: float,
    comparison_value: float,
) -> float:
    """Tính phần trăm tăng so với giá trị cơ sở."""
    if baseline_value == 0:
        raise ValueError("Không thể tính mức tăng khi giá trị cơ sở bằng 0.")

    return float(
        (comparison_value - baseline_value)
        / baseline_value
        * 100
    )


def create_season_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Tạo bảng bằng chứng chính cho hai nhóm mùa phát hành."""
    return (
        data.groupby("season_group")
        .agg(
            movie_count=("id", "size"),
            mean_revenue=("revenue", "mean"),
            median_revenue=("revenue", "median"),
            revenue_std=("revenue", "std"),
            minimum_revenue=("revenue", "min"),
            maximum_revenue=("revenue", "max"),
        )
        .reindex(SEASON_ORDER)
    )


def calculate_trimmed_mean(
    values: pd.Series,
    lower_quantile: float = 0.01,
    upper_quantile: float = 0.99,
) -> float:
    """Tính trung bình sau khi bỏ hai đuôi của phân phối."""
    if not 0 <= lower_quantile < upper_quantile <= 1:
        raise ValueError(
            "Phân vị phải thỏa mãn 0 <= cận dưới < cận trên <= 1."
        )

    numeric_values = pd.to_numeric(
        values,
        errors="coerce",
    ).dropna()
    if numeric_values.empty:
        raise ValueError("Không có giá trị số để tính trung bình cắt ngọn.")

    lower_bound = numeric_values.quantile(lower_quantile)
    upper_bound = numeric_values.quantile(upper_quantile)
    trimmed_values = numeric_values.loc[
        numeric_values.between(lower_bound, upper_bound)
    ]

    return float(np.mean(trimmed_values.to_numpy()))


def create_trimmed_mean_by_group(data: pd.DataFrame) -> pd.Series:
    """Tính trung bình cắt ngọn cho từng nhóm mùa."""
    return (
        data.groupby("season_group")["revenue"]
        .apply(calculate_trimmed_mean)
        .reindex(SEASON_ORDER)
        .rename("trimmed_mean_revenue")
    )


def create_month_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Tổng hợp số phim, trung bình và trung vị theo 12 tháng."""
    month_summary = (
        data.groupby(["release_month", "season_group"])
        .agg(
            movie_count=("id", "size"),
            mean_revenue=("revenue", "mean"),
            median_revenue=("revenue", "median"),
        )
        .reset_index()
        .sort_values("release_month")
    )
    month_summary["month_label"] = (
        "Tháng " + month_summary["release_month"].astype(str)
    )
    month_summary["mean_revenue_million_usd"] = (
        month_summary["mean_revenue"] / 1_000_000
    )

    return month_summary


def create_decade_check(
    data: pd.DataFrame,
    minimum_group_size: int = MINIMUM_GROUP_SIZE,
) -> pd.DataFrame:
    """Kiểm tra chênh lệch hai nhóm riêng theo từng thập niên."""
    group_counts = (
        data.groupby(["release_decade", "season_group"])
        .size()
        .unstack(fill_value=0)
        .reindex(columns=SEASON_ORDER, fill_value=0)
    )
    eligible_decades = group_counts.loc[
        group_counts.ge(minimum_group_size).all(axis=1)
    ].index
    mean_revenue = (
        data.loc[data["release_decade"].isin(eligible_decades)]
        .groupby(["release_decade", "season_group"])["revenue"]
        .mean()
        .unstack()
        .reindex(columns=SEASON_ORDER)
    )
    decade_check = mean_revenue.join(
        group_counts.add_suffix("_count")
    )
    decade_check["mean_uplift_percent"] = (
        (
            decade_check[PEAK_LABEL]
            - decade_check[OFFPEAK_LABEL]
        )
        / decade_check[OFFPEAK_LABEL]
        * 100
    )

    return decade_check


def evaluate_hypothesis_3(
    season_summary: pd.DataFrame,
    trimmed_mean_by_group: pd.Series,
    *,
    minimum_group_size: int = MINIMUM_GROUP_SIZE,
    required_uplift_percent: float = REQUIRED_UPLIFT_PERCENT,
) -> pd.DataFrame:
    """Áp dụng quy tắc Chấp nhận, Bác bỏ hoặc Chưa đủ bằng chứng."""
    mean_uplift = calculate_uplift_percent(
        season_summary.loc[OFFPEAK_LABEL, "mean_revenue"],
        season_summary.loc[PEAK_LABEL, "mean_revenue"],
    )
    median_uplift = calculate_uplift_percent(
        season_summary.loc[OFFPEAK_LABEL, "median_revenue"],
        season_summary.loc[PEAK_LABEL, "median_revenue"],
    )
    trimmed_uplift = calculate_uplift_percent(
        trimmed_mean_by_group.loc[OFFPEAK_LABEL],
        trimmed_mean_by_group.loc[PEAK_LABEL],
    )
    groups_are_large_enough = bool(
        season_summary["movie_count"]
        .ge(minimum_group_size)
        .all()
    )

    if not groups_are_large_enough:
        decision = "Chưa đủ bằng chứng"
        reason = "Một hoặc cả hai nhóm không đủ cỡ mẫu."
    elif (
        mean_uplift >= required_uplift_percent
        and trimmed_uplift >= 0
    ):
        decision = "Chấp nhận"
        reason = (
            "Trung bình vượt ngưỡng đặt trước và "
            "trung bình cắt ngọn không đảo chiều."
        )
    elif mean_uplift < required_uplift_percent:
        decision = "Bác bỏ"
        reason = "Trung bình không đạt ngưỡng đặt trước."
    else:
        decision = "Chưa đủ bằng chứng"
        reason = (
            "Trung bình đạt ngưỡng nhưng "
            "trung bình cắt ngọn đảo chiều."
        )

    return pd.DataFrame(
        [
            {
                "hypothesis_id": "H3_release_season_revenue",
                "decision": decision,
                "mean_uplift_percent": mean_uplift,
                "required_uplift_percent": required_uplift_percent,
                "median_uplift_percent": median_uplift,
                "trimmed_mean_uplift_percent": trimmed_uplift,
                "offpeak_movie_count": int(
                    season_summary.loc[
                        OFFPEAK_LABEL,
                        "movie_count",
                    ]
                ),
                "peak_movie_count": int(
                    season_summary.loc[
                        PEAK_LABEL,
                        "movie_count",
                    ]
                ),
                "reason": reason,
            }
        ]
    )
