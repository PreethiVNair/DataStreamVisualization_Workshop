from movies_data_load_and_queries.LoadMoviesData import movies
import matplotlib.pyplot as plt 

# Create a smaller dataset with the needed columns
movies_corr = movies[["revenue", "popularity"]].dropna().copy()

# Check correlation between revenue and popularity
correlation = movies_corr["revenue"].corr(movies_corr["popularity"])
print(f"Correlation between revenue and popularity: {correlation:.4f}")

# Plot revenue (X-axis) against popularity (Y-axis)

plt.figure(figsize=(10, 6))
plt.scatter(movies_corr["revenue"], movies_corr["popularity"], alpha=0.6)
plt.title("Revenue vs Popularity")
plt.xlabel("Revenue")
plt.ylabel("Popularity")
plt.grid(True)
plt.show()