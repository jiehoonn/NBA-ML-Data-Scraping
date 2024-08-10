import pandas as pd
import os

def load_and_clean_mvps(input_dir="output"):
    all_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.startswith("mvp_") and f.endswith(".csv")]
    
    df_list = []
    for file in all_files:
        df = pd.read_csv(file)
        df_list.append(df)
    
    mvps = pd.concat(df_list, ignore_index=True)
    
    # Assuming you need only specific columns:
    if "Player" in mvps.columns and "Year" in mvps.columns and "Pts Won" in mvps.columns and "Pts Max" in mvps.columns and "Share" in mvps.columns:
        mvps = mvps[["Player", "Year", "Pts Won", "Pts Max", "Share"]]
    return mvps