"""Visualisation for insight 2: the three-point revolution."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd


def plot_three_point_trend(
    trend: pd.DataFrame,
    output_path: str | Path = "figures/insight_2_three_point_revolution.png",
) -> Figure:
    """Plot per-team attempts and the share of shots taken from three."""
    if trend.empty:
        raise ValueError("The trend dataframe is empty.")

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    years = trend["season_start_year"]
    attempts = trend["avg_three_pa_per_team_game"]
    share = trend["three_pa_share_pct"]

    axes[0].plot(years, attempts, color="#e4572e", linewidth=2.8)
    axes[0].fill_between(years, attempts, color="#e4572e", alpha=0.13)
    axes[0].set_ylabel("3-point attempts\nper team per game")
    axes[0].annotate(
        f"{attempts.iloc[0]:.1f}",
        (years.iloc[0], attempts.iloc[0]),
        xytext=(8, 8),
        textcoords="offset points",
        fontweight="bold",
    )
    axes[0].annotate(
        f"{attempts.iloc[-1]:.1f}",
        (years.iloc[-1], attempts.iloc[-1]),
        xytext=(-34, 8),
        textcoords="offset points",
        fontweight="bold",
    )

    axes[1].plot(years, share, color="#2878b5", linewidth=2.8)
    axes[1].fill_between(years, share, color="#2878b5", alpha=0.13)
    axes[1].set_ylabel("3-point attempts\nas share of all FGA")
    axes[1].set_xlabel("NBA season (start year)")
    axes[1].annotate(
        f"{share.iloc[0]:.1f}%",
        (years.iloc[0], share.iloc[0]),
        xytext=(8, 8),
        textcoords="offset points",
        fontweight="bold",
    )
    axes[1].annotate(
        f"{share.iloc[-1]:.1f}%",
        (years.iloc[-1], share.iloc[-1]),
        xytext=(-42, 8),
        textcoords="offset points",
        fontweight="bold",
    )

    fig.suptitle(
        "The three-point revolution: from a few tries to nearly 4 in 10 shots",
        fontsize=16,
        fontweight="bold",
        y=0.99,
    )
    for axis in axes:
        axis.grid(axis="y", color="#d9d9d9", linewidth=0.8)
        axis.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(rect=(0, 0, 1, 0.96))

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=180, bbox_inches="tight")
    return fig
