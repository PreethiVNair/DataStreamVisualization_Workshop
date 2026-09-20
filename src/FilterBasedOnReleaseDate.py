import LoadMoviesData as lmd
import pandas as pd


# Make sure the date column is in datetime format
lmd.movies["release_date"] = pd.to_datetime(lmd.movies["release_date"], errors="coerce")

# Keep only the movies released in 2019
movies_2019 = lmd.movies[lmd.movies["release_date"].dt.year == 2019].copy()

# Show the results
print(movies_2019.head())