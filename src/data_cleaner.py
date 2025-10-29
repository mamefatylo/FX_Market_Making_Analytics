# src/data_cleaner.py

from pathlib import Path
import pandas as pd

def clean_fx_data(fx_data: dict,
                  numeric_cols: list | None = None,
                  combine: bool = False,
                  save_processed: bool = False,
                  processed_path: str | Path = "data/processed"):
    """
    Clean FX pair DataFrames with Bid/Ask/Volume columns, compute mid-prices.

    Parameters
    ----------
    fx_data : dict
        Mapping like {"EURUSD": df, "USDCHF": df}
    numeric_cols : list[str] | None
        Numeric columns to coerce to float. Defaults to ["Bid", "Ask", "High", "Low", "Volume"].
    combine : bool
        If True, return combined DataFrame of all pairs.
    save_processed : bool
        If True, save cleaned CSVs to processed_path.
    processed_path : str or Path
        Directory to save cleaned files.

    Returns
    -------
    cleaned_data : dict
        cleaned_data[pair] = cleaned dataframe
    combined_df : pd.DataFrame or None
        concatenated dataframe if combine==True else None
    """
    if numeric_cols is None:
        numeric_cols = ["Bid", "Ask", "High", "Low", "Volume"]

    cleaned_data = {}
    processed_path = Path(processed_path)
    if save_processed:
        processed_path.mkdir(parents=True, exist_ok=True)

    for pair_name, df in fx_data.items():
        temp = df.copy()

        # Convert numeric columns
        for col in numeric_cols:
            if col in temp.columns:
                temp[col] = pd.to_numeric(temp[col], errors="coerce")

        # Compute Mid price
        if "Bid" in temp.columns and "Ask" in temp.columns:
            temp["Mid"] = (temp["Bid"] + temp["Ask"]) / 2

        # Ensure Date column is datetime
        if "Date" in temp.columns:
            temp["Date"] = pd.to_datetime(temp["Date"], errors="coerce")
        else:
            temp["Date"] = pd.NaT

        # Drop rows missing critical data
        required = ["Date"]
        if "Bid" in temp.columns: required.append("Bid")
        if "Ask" in temp.columns: required.append("Ask")
        temp = temp.dropna(subset=required)

        # Sort by Date
        temp = temp.sort_values("Date").reset_index(drop=True)

        # Save processed CSV
        if save_processed:
            out_file = processed_path / f"{pair_name}_clean.csv"
            temp.to_csv(out_file, index=False)

        cleaned_data[pair_name] = temp

    # Optionally combine
    combined_df = None
    if combine:
        if cleaned_data:
            combined_df = pd.concat(list(cleaned_data.values()), ignore_index=True)
        else:
            combined_df = pd.DataFrame()

    return cleaned_data, combined_df

# Example usage:
# cleaned_fx, combined_df = clean_fx_data(fx_data, combine=True, save_processed=True)
