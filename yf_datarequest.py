from pathlib import Path
import pandas as pd
import yfinance as yf


def range_sort(reference_point: int, reference_end: int) -> list:
    reference_range = []
    while True:
        if reference_point == reference_end:
            reference_range.append(reference_end)
            return reference_range
        else:
            reference_range.append(reference_point)
            reference_point += 1


# Data entry and export
def export_data(ticker: str, reference_year: int) -> None:
    start_date = f"{reference_year}-01-01"
    end_date = f"{reference_year}-12-31"

    # Fetch data
    spy = yf.Ticker(ticker)

    data = spy.history(start=start_date, end=end_date)

    # Select OHLC columns
    ohlc_data = data[["Open", "High", "Low", "Close"]]


    # Save to CSV
    try:
        csv_filename = f"{folder_path}/{ticker}_{reference_year}_OHLC.csv"
    except:
        folder_path = Path(f"references/{ticker}")
        folder_path.mkdir(parents=True, exist_ok=True)
        csv_filename = f"{folder_path}/{ticker}_{reference_year}_OHLC.csv"
    ohlc_data.to_csv(csv_filename)

    print(f"OHLC data for SPY in {reference_year} saved to {csv_filename}")


def main() -> None:
    """
    Warning: No file scrutiny, exports into dump references folder.

    Requests OHLC data from yfinance.
    """
    ticker = input("Enter ticker: ").upper()
    reference_start = int(input("Start Range: "))
    reference_end = int(input("End Range: "))
    reference_range = range_sort(reference_start, reference_end)
    for reference_year in reference_range:
        export_data(ticker, reference_year)
    print('Exporting data has been collected.')

if __name__ == "__main__":
    main()