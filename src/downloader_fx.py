# downloader_fx.py

"""
Downloader for FX historical data from Dukascopy.
Downloads daily 1-minute CSVs and combines them into a single file per pair.

Author: Mame Faty Lo
"""

import requests
from pathlib import Path
import pandas as pd
from datetime import timedelta

def download_and_combine_fx(pair: str, start_date, end_date, save_path="data/raw/fx_full"):
    """
    Download daily 1-minute FX CSVs from Dukascopy and combine them.

    Parameters
    ----------
    pair : str
        FX pair code, e.g. "EURUSD"
    start_date : datetime.date
        Start date
    end_date : datetime.date
        End date
    save_path : str or Path
        Directory to save combined CSV
    """
    save_path = Path(save_path)
    save_path.mkdir(parents=True, exist_ok=True)
    
    all_dfs = []
    date = start_date
    
    while date <= end_date:
        # Dukascopy uses YYYY/MM/DD in URL
        url_date = date.strftime("%Y/%m/%d")
        # CSV filename format on Dukascopy
        file_url = f"https://www.dukascopy.com/datafeed/{pair}/{url_date}/1min.csv"
        
        try:
            r = requests.get(file_url)
            if r.status_code == 200:
                # Read CSV directly from content
                from io import StringIO
                df = pd.read_csv(StringIO(r.text), header=None)
                df.columns = ["Date", "Bid", "Ask", "Low", "High", "Volume"]
                
                # Parse date column
                df["Date"] = pd.to_datetime(df["Date"], format="%d.%m.%Y %H:%M:%S.%f UTC", errors="coerce")
                
                all_dfs.append(df)
                print(f"[OK] {pair} {date} downloaded ({len(df)} rows)")
            else:
                print(f"[WARN] {file_url} not found (status {r.status_code})")
        except Exception as e:
            print(f"[ERROR] {pair} {date} - {e}")
        
        date += timedelta(days=1)
    
    if all_dfs:
        combined = pd.concat(all_dfs, ignore_index=True)
        out_file = save_path / f"{pair}.csv"
        combined.to_csv(out_file, index=False)
        print(f"[OK] Combined CSV saved: {out_file} ({len(combined)} rows)")
    else:
        print(f"[WARN] No data downloaded for {pair}")


# Example usage (uncomment to run as script):
# if __name__ == "__main__":
#     from datetime import date
#     download_and_combine_fx("EURUSD", date(2025, 8, 1), date(2025, 10, 28))
#     download_and_combine_fx("USDCHF", date(2025, 8, 1), date(2025, 10, 28))
#     download_and_combine_fx("GBPUSD", date(2025, 8, 1), date(2025, 10, 28))
