# src/data_loader.py

from pathlib import Path
import pandas as pd

def load_fx_data(pairs, raw_path="data/raw/fx_full"):
    """
    Load combined FX CSVs into a dictionary of DataFrames.
    
    Parameters
    ----------
    pairs : list of str
        List of currency pairs to load, e.g., ["EURUSD", "USDCHF"]
    raw_path : str or Path
        Directory where combined CSVs are saved.
    
    Returns
    -------
    fx_data : dict
        Dictionary where keys are pair names and values are DataFrames with parsed columns:
        Date (datetime), Bid, Ask, Low, High, Volume.
    """
    fx_data = {}
    raw_path = Path(raw_path)
    
    for pair in pairs:
        csv_file = raw_path / f"{pair}.csv"
        if csv_file.exists():
            df = pd.read_csv(csv_file)
            
            # Parse date properly
            if "Date" in df.columns:
                df["Date"] = pd.to_datetime(df["Date"], format="%d.%m.%Y %H:%M:%S.%f UTC", errors="coerce")
            
            # Ensure numeric columns are floats
            for col in ["Bid", "Ask", "Low", "High", "Volume"]:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors="coerce")
            
            fx_data[pair] = df
            print(f"[INFO] Loaded {pair}: {len(df)} rows, columns: {list(df.columns)}")
            display(df.head(2))
        else:
            print(f"[WARNING] CSV not found for {pair}: {csv_file}")
    
    return fx_data

# Example usage:
# pairs = ["EURUSD", "USDCHF", "GBPUSD"]
# fx_data = load_fx_data(pairs)
