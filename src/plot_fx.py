# src/plot_fx.py

from pathlib import Path
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# Default Plotly template
pio.templates.default = "plotly_dark"
px.defaults.width = 900
px.defaults.height = 520

# -------------------------
# Helper functions
# -------------------------

def compute_daily_returns(df: pd.DataFrame, price_col: str = "Mid") -> pd.Series:
    """Compute daily returns from Mid price."""
    p = pd.to_numeric(df[price_col], errors="coerce")
    returns = p.pct_change()
    return returns

def compute_rolling_volatility(df: pd.DataFrame, price_col: str = "Mid", window: int = 21) -> pd.Series:
    """Compute rolling annualised volatility of Mid prices."""
    daily_ret = compute_daily_returns(df, price_col)
    rolling_std = daily_ret.rolling(window=window, min_periods=1).std()
    annualised_vol = rolling_std * np.sqrt(252)  # 252 trading days
    return annualised_vol

def compute_bid_ask_spread(df: pd.DataFrame) -> pd.Series:
    """Compute bid-ask spread."""
    if "Bid" in df.columns and "Ask" in df.columns:
        return df["Ask"] - df["Bid"]
    else:
        return pd.Series(np.nan, index=df.index)

# -------------------------
# Plotting functions
# -------------------------

def plot_mid_price_trends(df: pd.DataFrame, pair_col="Pair", date_col="Date", price_col="Mid"):
    plot_df = df.copy()
    plot_df[date_col] = pd.to_datetime(plot_df[date_col], errors="coerce")
    plot_df[price_col] = pd.to_numeric(plot_df[price_col], errors="coerce")
    if pair_col not in plot_df.columns:
        plot_df[pair_col] = "Series"
    fig = px.line(plot_df, x=date_col, y=price_col, color=pair_col,
                  title="Mid Price Trends",
                  labels={date_col: "Date", price_col: "Mid Price", pair_col: "Currency Pair"})
    fig.update_layout(legend_title_text="Pair", hovermode="x unified")
    return fig

def plot_bid_ask_spread(df: pd.DataFrame, pair_col="Pair", date_col="Date"):
    plot_df = df.copy()
    plot_df[date_col] = pd.to_datetime(plot_df[date_col], errors="coerce")
    plot_df["Spread"] = compute_bid_ask_spread(plot_df)
    if pair_col not in plot_df.columns:
        plot_df[pair_col] = "Series"
    fig = px.line(plot_df, x=date_col, y="Spread", color=pair_col,
                  title="Bid-Ask Spread",
                  labels={date_col: "Date", "Spread": "Bid-Ask Spread", pair_col: "Currency Pair"})
    fig.update_layout(legend_title_text="Pair", hovermode="x unified")
    return fig

def plot_returns(df: pd.DataFrame, pair_col="Pair", date_col="Date", price_col="Mid"):
    plot_df = df.copy()
    plot_df[date_col] = pd.to_datetime(plot_df[date_col], errors="coerce")
    plot_df["Return"] = plot_df.groupby(pair_col)[price_col].pct_change()
    fig = px.line(plot_df, x=date_col, y="Return", color=pair_col,
                  title="Daily Returns (from Mid Price)",
                  labels={date_col: "Date", "Return": "Daily Return", pair_col: "Currency Pair"})
    fig.update_layout(legend_title_text="Pair", hovermode="x unified")
    return fig

def plot_rolling_volatility(df: pd.DataFrame, pair_col="Pair", date_col="Date", price_col="Mid", window=21):
    plot_df = df.copy()
    plot_df[date_col] = pd.to_datetime(plot_df[date_col], errors="coerce")
    vol_list = []
    for pair, g in plot_df.groupby(pair_col):
        g_sorted = g.sort_values(date_col)
        g_sorted["Volatility"] = compute_rolling_volatility(g_sorted, price_col=price_col, window=window)
        vol_list.append(g_sorted[[date_col, pair_col, "Volatility"]])
    vol_df = pd.concat(vol_list, ignore_index=True)
    fig = px.line(vol_df, x=date_col, y="Volatility", color=pair_col,
                  title=f"Rolling Annualised Volatility (window={window})",
                  labels={date_col: "Date", "Volatility": "Annualised Volatility", pair_col: "Currency Pair"})
    fig.update_layout(legend_title_text="Pair", hovermode="x unified")
    return fig

# -------------------------
# Save utility
# -------------------------
def save_plot(fig, path: str | Path):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.suffix.lower() == ".html":
        fig.write_html(str(p))
    else:
        fig.write_image(str(p))
    print(f"[INFO] Saved figure to {p}")
