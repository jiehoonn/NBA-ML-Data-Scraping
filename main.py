from data_loader import load_and_clean_mvps
import pandas as pd

if __name__ == "__main__":
    mvps = load_and_clean_mvps("output")  # This points to the directory where `mvp_{year}.csv` files are stored
    # Save the combined DataFrame
    mvps.to_csv("combined_mvps.csv", index=False)

    # In the future: Need to obtain more data that impacts MVP Vote scores
    # For example, Team performance, Player Efficiency Rating, Win Shares, Box Plus-Minus, etc.