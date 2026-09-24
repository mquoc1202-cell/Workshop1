"""Điều phối toàn bộ quy trình của Giả thuyết 3."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from .analyzer import (
    create_decade_check,
    create_month_summary,
    create_season_summary,
    create_trimmed_mean_by_group,
    evaluate_hypothesis_3,
)
from .data_preparer import prepare_hypothesis_3_data
from .visualizer import (
    plot_monthly_revenue,
    plot_season_revenue,
)


def run_hypothesis_3(
    clean_data: pd.DataFrame,
    *,
    processed_folder: str | Path,
    table_folder: str | Path,
    figure_folder: str | Path,
) -> dict[str, object]:
    """Chạy H3 từ dữ liệu sạch FR04 và xuất toàn bộ bằng chứng."""
    processed_path = Path(processed_folder)
    table_path = Path(table_folder)
    figure_path = Path(figure_folder)
    processed_path.mkdir(parents=True, exist_ok=True)
    table_path.mkdir(parents=True, exist_ok=True)
    figure_path.mkdir(parents=True, exist_ok=True)

    hypothesis_data, quality_trace, input_checks = (
        prepare_hypothesis_3_data(clean_data)
    )
    season_summary = create_season_summary(hypothesis_data)
    trimmed_mean = create_trimmed_mean_by_group(hypothesis_data)
    month_summary = create_month_summary(hypothesis_data)
    decade_check = create_decade_check(hypothesis_data)
    evaluation = evaluate_hypothesis_3(
        season_summary,
        trimmed_mean,
    )

    primary_figure, _ = plot_season_revenue(
        season_summary,
        figure_path / "hypothesis3_release_season_revenue.png",
    )
    monthly_figure, _ = plot_monthly_revenue(
        month_summary,
        figure_path / "hypothesis3_monthly_revenue.png",
    )
    plt.close(primary_figure)
    plt.close(monthly_figure)

    hypothesis_data.to_csv(
        processed_path / "hypothesis3_release_season_clean.csv",
        index=False,
    )
    quality_trace.to_csv(
        table_path / "hypothesis3_quality_trace.csv",
        index=False,
    )
    season_summary.to_csv(
        table_path / "hypothesis3_release_season_summary.csv"
    )
    trimmed_mean.to_csv(
        table_path / "hypothesis3_trimmed_mean.csv"
    )
    month_summary.to_csv(
        table_path / "hypothesis3_month_summary.csv",
        index=False,
    )
    decade_check.to_csv(
        table_path / "hypothesis3_decade_check.csv"
    )
    evaluation.to_csv(
        table_path / "hypothesis3_evaluation.csv",
        index=False,
    )

    return {
        "clean_data": hypothesis_data,
        "quality_trace": quality_trace,
        "input_checks": input_checks,
        "season_summary": season_summary,
        "trimmed_mean": trimmed_mean,
        "month_summary": month_summary,
        "decade_check": decade_check,
        "evaluation": evaluation,
    }
