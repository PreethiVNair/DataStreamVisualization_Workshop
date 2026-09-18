import LoadSpotifyMusicFile as lsf
import pandas as pd

# Make sure the date column is in datetime format
lsf.songs["release_date"] = pd.to_datetime(lsf.songs["release_date"], errors="coerce")

# Keep only the movies released in 2019
songs_2019 = lsf.songs[lsf.songs["release_date"].dt.year == 2019].copy()

# Show the results
songs_2019.head()