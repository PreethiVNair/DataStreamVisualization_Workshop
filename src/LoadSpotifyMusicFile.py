import pandas as pd
from pathlib import Path

pd.set_option('display.max_columns', None)

def spotify_data_collect():
    root = Path(__file__).resolve().parent
    csv_path = root /"data" / "data.csv"
    songs = pd.read_csv(csv_path, low_memory=False)
   
    return songs

songs = spotify_data_collect()
