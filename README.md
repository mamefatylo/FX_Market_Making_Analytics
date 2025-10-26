# FX Market Making Analytics

**Author:** Mame Faty Lo | 1290, Versoix | mamefatylo.b@gmail.com  

This portfolio demonstrates **FX market making, liquidity analysis, and trading analytics** using Python.  
<<<<<<< HEAD
It includes real market data for currency pairs, interactive visualizations, and simulations of market making concepts.  

=======

It includes real market data for currency pairs, interactive visualizations, and simulations of market making concepts.  


>>>>>>> 6653c1e (Update .gitignore and other local changes)
Fully reproducible via Conda (`environment.yml`) for hands-on exploration.

---

## Overview
<<<<<<< HEAD
  
- Analyze real **FX market data** for multiple currency pairs  
=======

Hi! In this project, I:

- Analyze **FX data** for 8 currency pairs  
>>>>>>> 6653c1e (Update .gitignore and other local changes)
- Explore **bid-ask spreads, mid-prices, volatility, and order book behavior**  
- Simulate **market making concepts** in Python  
- Generate **interactive charts and reports** to support insights  

<<<<<<< HEAD
I designed this portfolio to be practical, clean, and easy for anyone to run.

---

## Skills and Concepts Demonstrated
=======
I wanted this portfolio to be practical, clean, and something that anyone can run easily.

---

## Skills and Concepts I Demonstrate
>>>>>>> 6653c1e (Update .gitignore and other local changes)

| Concept | What It Means |
|---------|---------------|
| **Market Making** | Placing buy and sell quotes to provide liquidity and earn the spread. |
| **Liquidity** | How easily a currency can be bought or sold without drastically moving its price. |
| **Bid-Ask Spread** | Difference between the highest buy price and the lowest sell price; market makers profit from this. |
| **Mid-Price** | The average of bid and ask prices, used as a reference point. |
<<<<<<< HEAD
| **Volatility** | Measures how much the price moves over time; calculated from mid-price returns. |
=======
| **Volatility** | Measures how much the price moves over time; I calculate it from mid-price returns. |
>>>>>>> 6653c1e (Update .gitignore and other local changes)
| **Order Book Dynamics** | Shows current buy/sell orders and how market pressure is distributed. |
| **Market Order vs Limit Order** | Market orders execute immediately; limit orders wait for a specific price. |

---

## Project Structure

<<<<<<< HEAD
```text
=======

>>>>>>> 6653c1e (Update .gitignore and other local changes)
fx-market-making-analytics/
├── data/
│   ├── raw/            # Raw FX data
│   └── processed/      # Cleaned and feature-engineered data
├── notebooks/
│   └── fx_market_making.ipynb
├── reports/
<<<<<<< HEAD
│   ├── summaries/      # Written analysis, key takeaways
│   └── figures/        # Charts, plots, interactive visuals
├── scripts/            # Any helper Python scripts
├── environment.yml     # Conda environment dependencies
├── README.md
└── .gitignore
```
=======
│   ├── charts/      
│   └── summaries/         # Saved PNG/PDF/HTML
├── environment.yml      # Conda environment dependencies
├── README.md
└── .gitignore

>>>>>>> 6653c1e (Update .gitignore and other local changes)
---

## Setup Instructions (Conda)

1. Clone the repository:

```
git clone <repository_url>
cd fx-market-making-analytics
<<<<<<< HEAD
```
=======
>>>>>>> 6653c1e (Update .gitignore and other local changes)

2. **Create and activate the environment**:

```
conda env create -f environment.yml
<<<<<<< HEAD
conda activate fx_market_making_env
```
=======

conda activate fx_market_making_env
>>>>>>> 6653c1e (Update .gitignore and other local changes)

3. **(Optional) Update packages**:

```
conda env update --file environment.yml --prune
<<<<<<< HEAD
```
=======

>>>>>>> 6653c1e (Update .gitignore and other local changes)

---

## How to Run

1. Activate the Conda environment (see above)
<<<<<<< HEAD
2. Open Jupyter and navigate to `notebooks/fx_market_making.ipynb
=======
2. Open Jupyter and navigate to notebooks/fx_market_making.ipynb
>>>>>>> 6653c1e (Update .gitignore and other local changes)


```
jupyter notebook
<<<<<<< HEAD
```

3. Follow the notebook cell by cell.
- Data is loaded from `data/raw/` and saved in `data/processed/`.
- Summaries and figures are saved automatically in `reports/summaries/` and `reports/figures/`.
=======

3. Follow the notebook cell by cell.
- Data is loaded from data/raw/ and saved in data/processed/.
- Summaries and figures are saved automatically in reports/summaries/ and reports/figures/.
>>>>>>> 6653c1e (Update .gitignore and other local changes)


---

## Data Sources

- Yahoo Finance (yfinance) for historical FX data
- Currency pairs relevant to Swissquote: EUR/USD, GBP/USD, USD/CHF, etc.
- Data includes OHLC prices and trading volume
- Notebook includes preprocessing, feature creation, and interactive visualizations


---

## Glossary of Key Terms
<<<<<<< HEAD

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
=======
**Market Making**: Placing buy/sell orders to provide liquidity and earn the spread
**Liquidity**: How easy it is to trade without moving the price
**Bid Price**: Highest price a buyer will pay
	•	Ask Price: Lowest price a seller will accept
	•	Spread: Difference between ask and bid
	•	Mid-Price: (Bid + Ask)/2
	•	Volatility: How much price moves over time
	•	Order Book: Shows all current buy and sell orders
	•	Market Order: Executes immediately at the best price
	•	Limit Order: Executes only at a specific price or better

⸻

Why This Matters

This project shows that I can:
	•	Work with real FX market data
	•	Apply quantitative analysis to trading strategies
	•	Build Python tools and visualizations for decision-making
	•	Understand market microstructure, liquidity, and risk concepts

It’s a portfolio piece that directly demonstrates skills for a trading internship while being reproducible and professional.

⸻

Conclusion

I’m really excited about FX markets and quantitative finance. This portfolio captures both my curiosity and my ability to code, analyze, and visualize trading data.

It’s fully ready to submit for the Swissquote FX & DA Trading Internship, and it’s also a foundation I can continue to build on as I learn more about market making and liquidity analytics.
>>>>>>> 6653c1e (Update .gitignore and other local changes)
