# FX Market Making Analytics

**Author:** Mame Faty Lo

In this project, I:

- Analyse **FX data** for multiple currency pairs
- Explore **bid-ask spreads, mid-prices, volatility, and market microstructure**
- Simulate **market-making concepts** in Python
- Generate **interactive charts and reports** to support insights

This notebook is designed to be practical, reproducible via Conda (`fx_env.yml`) for hands-on exploration.

---

## Skills and Concepts Demonstrated

| Concept | What It Means |
|---------|---------------|
| **Market Making** | Placing buy and sell quotes to provide liquidity and earn the spread. |
| **Liquidity** | How easily a currency can be traded without drastically moving its price. |
| **Bid-Ask Spread** | Difference between the highest buy price and lowest sell price; a key metric for market makers. |
| **Mid-Price** | The average of bid and ask prices, used as a reference point. |
| **Volatility** | Measures price movement over time; calculated from mid-price returns. |
| **Market Microstructure** | Understanding how orders, spreads, and liquidity interact in the market. |
| **Market vs Limit Orders** | Market orders execute immediately; limit orders wait for a specific price. |

---

## Project Structure

fx-market-making-analytics/
├── data/
│ ├── raw/                      # Raw FX data
│ └── processed/                # Cleaned and feature-engineered data
├── notebooks/
│ └── fx_market_making.ipynb
├── reports/
│ ├── summaries/                # Written key takeaways
│ └── figures/                  # Charts, plots, interactive visuals
├── scripts/                    # Any helper Python scripts
├── fx_env.yml                  # Conda environment dependencies
├── README.md
└── .gitignore

---

## Setup Instructions (Conda)

```bash
git clone <repository_url>
cd fx-market-making-analytics

conda env create -f fx_env.yml
conda activate fx_env

# (Optional) Update packages
conda env update --file fx_env.yml --prune

```

---

## How to Run

1. Activate the Conda environment (see above)  

2. Open Jupyter and navigate to `notebooks/fx_market_making.ipynb`  

```
jupyter notebook

```


3. Follow the notebook cell by cell:  
- Data is loaded from `data/raw/` and saved in `data/processed/`  
- Summaries and figures are saved automatically in `reports/summaries/` and `reports/charts/`  

---

## Data Sources

- Yahoo Finance (via `yfinance`) for historical FX data  
- Currency pairs relevant to Swissquote: EUR/USD, GBP/USD, USD/CHF, etc.  
- Includes OHLC prices, trading volume, and preprocessing for analysis  

---

## Why This Matters

This project demonstrates that I can:

- Work with real FX market data  
- Apply quantitative analysis to trading strategies  
- Build Python tools and visualisations for decision-making  
- Understand market microstructure, liquidity, and risk concepts  

It is **a work in progress**, but it already showcases my curiosity, coding skills, and ability to analyse and visualise trading data.

---

## Future Work

- Liquidity assessment and bid-ask spread analysis  
- Order book analysis and microstructure modelling  
- Integration of predictive models for FX trends


