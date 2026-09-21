import pandas as pd
from pathlib import Path

#pd.set_option('display.max_columns', None)

def movies_data_collect():
    root = Path(__file__).resolve().parent.parent
    csv_path = root /"data" / "TMDB_movie_dataset_v11.csv"
    movies = pd.read_csv(csv_path, low_memory=False)
    print(movies.head(5))
    return movies

movies = movies_data_collect()
