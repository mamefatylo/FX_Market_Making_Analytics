# FX Market Making Analytics

**Author:** Mame Faty Lo | 1290, Versoix | mamefatylo.b@gmail.com  

This portfolio demonstrates **FX market making, liquidity analysis, and trading analytics** using Python.  
It includes real market data for currency pairs, interactive visualizations, and simulations of market making concepts.  

Fully reproducible via Conda (`environment.yml`) for hands-on exploration.

---

## Overview
  
- Analyze real **FX market data** for multiple currency pairs  
- Explore **bid-ask spreads, mid-prices, volatility, and order book behavior**  
- Simulate **market making concepts** in Python  
- Generate **interactive charts and reports** to support insights  

I designed this portfolio to be practical, clean, and easy for anyone to run.

---

## Skills and Concepts Demonstrated

| Concept | What It Means |
|---------|---------------|
| **Market Making** | Placing buy and sell quotes to provide liquidity and earn the spread. |
| **Liquidity** | How easily a currency can be bought or sold without drastically moving its price. |
| **Bid-Ask Spread** | Difference between the highest buy price and the lowest sell price; market makers profit from this. |
| **Mid-Price** | The average of bid and ask prices, used as a reference point. |
| **Volatility** | Measures how much the price moves over time; calculated from mid-price returns. |
| **Order Book Dynamics** | Shows current buy/sell orders and how market pressure is distributed. |
| **Market Order vs Limit Order** | Market orders execute immediately; limit orders wait for a specific price. |

---

## Project Structure

```text
fx-market-making-analytics/
├── data/
│   ├── raw/            # Raw FX data
│   └── processed/      # Cleaned and feature-engineered data
├── notebooks/
│   └── fx_market_making.ipynb
├── reports/
│   ├── summaries/      # Written analysis, key takeaways
│   └── figures/        # Charts, plots, interactive visuals
├── scripts/            # Any helper Python scripts
├── environment.yml     # Conda environment dependencies
├── README.md
└── .gitignore
```
---

## Setup Instructions (Conda)

1. Clone the repository:

```
git clone <repository_url>
cd fx-market-making-analytics
```

2. **Create and activate the environment**:

```
conda env create -f environment.yml
conda activate fx_market_making_env
```

3. **(Optional) Update packages**:

```
conda env update --file environment.yml --prune
```

---

## How to Run

1. Activate the Conda environment (see above)
2. Open Jupyter and navigate to `notebooks/fx_market_making.ipynb


```
jupyter notebook
```

3. Follow the notebook cell by cell.
- Data is loaded from `data/raw/` and saved in `data/processed/`.
- Summaries and figures are saved automatically in `reports/summaries/` and `reports/figures/`.


---

## Data Sources

- Yahoo Finance (yfinance) for historical FX data
- Currency pairs relevant to Swissquote: EUR/USD, GBP/USD, USD/CHF, etc.
- Data includes OHLC prices and trading volume
- Notebook includes preprocessing, feature creation, and interactive visualizations


---

## Glossary of Key Terms

**Market Making**: Placing buy/sell orders to provide liquidity and earn the spread

**Liquidity**: How easy it is to trade without moving the price

**Bid Price**: Highest price a buyer will pay

**Ask Price**: Lowest price a seller will accept

**Spread**: Difference between ask and bid

**Mid-Price**: (Bid + Ask)/2

**Volatility**: How much price moves over time

**Order Book**: Shows all current buy and sell orders

**Market Order**: Executes immediately at the best price

**Limit Order**: Executes only at a specific price or better

---

## Conclusion

This portfolio showcases my curiosity, coding skills, and ability to analyze and visualize financial data. It demonstrates the key skills relevant to the Swissquote FX & DA Trading Internship and provides a solid foundation to build on as I continue learning about FX markets and quantitative finance.
