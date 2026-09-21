from movies_data_load_and_queries.LoadMoviesData import movies

# Filter for movies with revenue over 1 million
movies_revenue_over_1m = movies[movies["revenue"] > 1000000].copy()

# Show the results
print(movies_revenue_over_1m.head())