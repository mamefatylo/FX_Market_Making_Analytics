from src.data_loader import load_fx_data

def test_loader():
    pairs = ["USD_CHF", "EUR_USD"]
    fx_data = load_fx_data(pairs)
    assert isinstance(fx_data, dict), "Loader should return a dict"
    for pair in pairs:
        assert pair in fx_data, f"{pair} missing from loader output"
        assert len(fx_data[pair]) > 0, f"{pair} loaded 0 rows"

if __name__ == "__main__":
    test_loader()
    print("Loader test passed!")