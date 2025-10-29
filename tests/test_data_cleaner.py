from src.data_loader import load_fx_data
from src.data_cleaner import clean_fx_data

def test_cleaner():
    pairs = ["USD_CHF", "EUR_USD"]
    fx_data = load_fx_data(pairs)
    cleaned_data, combined_df = clean_fx_data(fx_data, combine=True)
    assert isinstance(cleaned_data, dict), "Cleaner should return dict"
    for pair in pairs:
        assert pair in cleaned_data, f"{pair} missing from cleaned_data"
        assert len(cleaned_data[pair]) > 0, f"{pair} cleaned 0 rows"
    assert not combined_df.empty, "Combined DataFrame is empty"

if __name__ == "__main__":
    test_cleaner()
    print("Cleaner test passed!")