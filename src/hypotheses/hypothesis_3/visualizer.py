"""Các biểu đồ bằng chứng cho Giả thuyết 3."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.patches import Patch

from .config import (
    OFFPEAK_LABEL,
    PEAK_LABEL,
    REQUIRED_UPLIFT_PERCENT,
    SEASON_ORDER,
)


def _save_figure(
    figure: plt.Figure,
    output_path: str | Path | None,
) -> Path | None:
    """Lưu hình nếu có đường dẫn đầu ra."""
    if output_path is None:
        return None

    figure_path = Path(output_path)
    figure_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(
        figure_path,
        dpi=300,
        bbox_inches="tight",
    )
    return figure_path


def plot_season_revenue(
    season_summary: pd.DataFrame,
    output_path: str | Path | None = None,
    *,
    required_uplift_percent: float = REQUIRED_UPLIFT_PERCENT,
) -> tuple[plt.Figure, plt.Axes]:
    """Vẽ doanh thu trung bình của nhóm Cao điểm và Thấp điểm."""
    plot_data = season_summary.reset_index().copy()
    plot_data["mean_revenue_million_usd"] = (
        plot_data["mean_revenue"] / 1_000_000
    )
    threshold = (
        season_summary.loc[OFFPEAK_LABEL, "mean_revenue"]
        * (1 + required_uplift_percent / 100)
        / 1_000_000
    )

    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"
    plt.rcParams["axes.unicode_minus"] = False

    figure, axis = plt.subplots(figsize=(9, 6))
    sns.barplot(
        data=plot_data,
        x="season_group",
        y="mean_revenue_million_usd",
        order=SEASON_ORDER,
        hue="season_group",
        palette={
            OFFPEAK_LABEL: "#4C78A8",
            PEAK_LABEL: "#F28E2B",
        },
        legend=False,
        errorbar=None,
        ax=axis,
    )
    axis.axhline(
        threshold,
        color="#D62728",
        linestyle="--",
        linewidth=1.5,
        label=(
            f"Ngưỡng {100 + required_uplift_percent:.0f}% "
            "doanh thu trung bình nhóm Thấp điểm"
        ),
    )

    ordered_rows = (
        plot_data.set_index("season_group").loc[list(SEASON_ORDER)]
    )
    for bar, row in zip(axis.patches, ordered_rows.itertuples()):
        axis.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            (
                f"{bar.get_height():,.1f} triệu USD\n"
                f"Số phim={row.movie_count:,}"
            ),
            ha="center",
            va="bottom",
        )

    axis.set_title(
        "Giả thuyết 3: Doanh thu trung bình theo mùa phát hành"
    )
    axis.set_xlabel("Nhóm mùa phát hành")
    axis.set_ylabel("Doanh thu trung bình (triệu USD)")
    axis.set_ylim(bottom=0)
    axis.legend()
    figure.tight_layout()
    _save_figure(figure, output_path)

    return figure, axis


def plot_monthly_revenue(
    month_summary: pd.DataFrame,
    output_path: str | Path | None = None,
) -> tuple[plt.Figure, plt.Axes]:
    """Vẽ doanh thu trung bình cho 12 tháng phát hành."""
    colors = {
        OFFPEAK_LABEL: "#4C78A8",
        PEAK_LABEL: "#F28E2B",
    }
    bar_colors = month_summary["season_group"].map(colors)

    sns.set_theme(style="whitegrid")
    plt.rcParams["font.family"] = "DejaVu Sans"
    plt.rcParams["axes.unicode_minus"] = False

    figure, axis = plt.subplots(figsize=(13, 7))
    bars = axis.bar(
        month_summary["month_label"],
        month_summary["mean_revenue_million_usd"],
        color=bar_colors,
    )
    for bar, row in zip(bars, month_summary.itertuples()):
        axis.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            (
                f"{row.mean_revenue_million_usd:,.1f}\n"
                f"Số phim={row.movie_count:,}"
            ),
            ha="center",
            va="bottom",
            fontsize=9,
        )

    axis.set_title(
        "Giả thuyết 3: Doanh thu trung bình theo từng tháng phát hành"
    )
    axis.set_xlabel("Tháng phát hành")
    axis.set_ylabel("Doanh thu trung bình (triệu USD)")
    axis.set_ylim(bottom=0)
    axis.legend(
        handles=[
            Patch(color=colors[OFFPEAK_LABEL], label=OFFPEAK_LABEL),
            Patch(color=colors[PEAK_LABEL], label=PEAK_LABEL),
        ],
        title="Nhóm mùa",
    )
    figure.tight_layout()
    _save_figure(figure, output_path)

    return figure, axis
