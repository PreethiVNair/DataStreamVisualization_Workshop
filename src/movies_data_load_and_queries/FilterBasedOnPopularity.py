import movies_data_load_and_queries.LoadMoviesData as lmd

# Filter for movies with popularity greater than 100
movies_popularity_over_100 = lmd.movies[lmd.movies["popularity"] > 100].copy()

# Show the results
print(movies_popularity_over_100.head())