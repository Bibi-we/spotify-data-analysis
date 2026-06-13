import pandas as pd 

import matplotlib.pyplot as plt 

import seaborn as sns 

import sqlite3 


df = pd.read_csv('data/tracks.csv') # load the dataset 
# =================================
# SQL ANALYSIS 
# =================================
conn = sqlite3.connect('data/tracks.db')
df.to_sql('tracks', conn, if_exists='replace', index=False) 

# Top 10 songs by popularity using SQL

query = """
SELECT name, popularity
FROM tracks
ORDER BY popularity DESC
LIMIT 10
"""

top_songs_sql = pd.read_sql_query(query, conn)

print(top_songs_sql)

# Export to CSV
top_songs_sql.to_csv('output/top_songs_by_popularity.csv', index=False) 

# Top artists by average popularity

query = """
SELECT artists,
       AVG(popularity) AS avg_popularity
FROM tracks
GROUP BY artists
ORDER BY avg_popularity DESC
LIMIT 10
"""

top_artists_sql = pd.read_sql_query(query, conn)

print(top_artists_sql)

# Export to CSV 
top_artists_sql.to_csv('output/top_artists_by_popularity.csv', index=False)


# top 10 Artists with most songs

query = """
SELECT artists,
       COUNT(*) AS song_count
FROM tracks
GROUP BY artists
ORDER BY song_count DESC
LIMIT 10
"""

artist_song_count_sql = pd.read_sql_query(query, conn)

print(artist_song_count_sql)

# Export to CSV
artist_song_count_sql.to_csv('output/top_artists_by_song_count.csv', index=False)

# top 10 Artists by average energy

query = """
SELECT artists,
       AVG(energy) AS avg_energy
FROM tracks
GROUP BY artists
ORDER BY avg_energy DESC
LIMIT 10
"""

artist_energy_sql = pd.read_sql_query(query, conn)

print(artist_energy_sql)

# Export to CSV 
artist_energy_sql.to_csv('output/top_artists_by_energy.csv', index=False) 



conn.close() 


# print(df.head()) # first five rows 

# print(df.shape) # number of rows and columns

# print(df.columns) # column names 

# print(df.dtypes) # data types of each column

# print(df.isnull().sum()) # missing values in each column

# # exploring the data further 
# print(df['popularity'].describe()) # summary statistics for the popularity column
# print(df[["danceability"]].describe()) # detailed statistics for danceability only
# print(df[["energy"]].describe()) # detailed statistics for energy only
# print(df[["tempo"]].describe()) # detailed statistics for tempo only


# top_songs = df[['name', 'popularity']].sort_values(by='popularity', ascending=False) # top songs by popularity
# print(top_songs.head(10)) # display top 10 popular songs

# visualize the top 10 popular song 

# top_10  = top_songs.head(10)

# plt.figure(figsize=(10,5))
# plt.barh(top_10['name'], top_10['popularity'])
# plt.xlabel('popularity')
# plt.title('top 10 popular songs')
# plt.tight_layout()

# plt.savefig('images/top_10_songs.png') # save the figure png 

# popularity distribution visualization
plt.figure(figsize=(10,5)) # set figure size 
plt.hist(df['popularity'], bins=30, color='blue', alpha=0.7) # create histogram
plt.xlabel('Popularity') # set x-label
plt.ylabel('Frequency') # set y-label 
plt.title('Popularity Distribution') # set title
plt.tight_layout() # adjust layout 
plt.savefig('images/popularity_distribution.png') # save the figure png

# popularity vs danceability scatterplot 
plt.figure(figsize=(10,5))
plt.scatter(df['danceability'], df['popularity'], alpha=0.3)

plt.xlabel('Danceability')
plt.ylabel('Popularity')
plt.title('Popularity vs Danceability')

plt.tight_layout()
plt.savefig('images/popularity_vs_danceability.png')

# popularity vs energy scatterplot
plt.figure(figsize=(10,5))
plt.scatter(df['energy'], df['popularity'], alpha=0.3)

plt.xlabel('Energy')
plt.ylabel('Popularity')
plt.title('Popularity vs Energy')

plt.tight_layout()
plt.savefig('images/popularity_vs_energy.png') 

# correlation analysis & Matrix 

correlation_matrix = df[
    ['popularity', 'danceability', 'energy', 'tempo']
].corr() # calculate correlation matrix

print(correlation_matrix) # display correlation matrix 


# correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')

plt.tight_layout()
plt.savefig('images/correlation_heatmap.png')



# artist analysis/ Top artists by Average Popularity 

artist_popularity = (
    df.groupby('artists')['popularity'] # groups all songs by artist
    .mean() # calculates average popularity
    .sort_values(ascending=False) # sorts values in descending order
)

print(artist_popularity.head(10)) # display top 10 artists by average popularity 

# visualize top 10 artists by average popularity
top_10_artists = artist_popularity.head(10) # select top 10 artists 

plt.figure(figsize=(10,5))
top_10_artists.sort_values().plot(kind='barh')

plt.xlabel('Average Popularity')
plt.ylabel('Artist')
plt.title('Top 10 Artists by Average Popularity')

plt.tight_layout()

plt.savefig('images/top_10_artists.png')

# artists with the most songs 

artist_song_count = (
    df.groupby('artists')['name']
    .count() # counts number of songs for each artist
    .sort_values(ascending=False)
)

print(artist_song_count.head(10)) # display top 10 artists by number of songs

# visualize top 10 artists by number of songs
top_artists_songs = artist_song_count.head(10)# select top 10 artists by number of songs

plt.figure(figsize=(10,5))

top_artists_songs.sort_values().plot(kind='barh') 

plt.xlabel('Number of Songs')
plt.ylabel('Artist')
plt.title('Top 10 Artists by Number of Songs')

plt.tight_layout()

plt.savefig('images/top_10_artists_by_songs.png')

# Average Energy by Artist
artist_energy = (
    df.groupby('artists')['energy']
    .mean()
    .sort_values(ascending=False)
)

print(artist_energy.head(10)) # display top 10 artists by average energy

# visualize top 10 artists by average energy
top_artist_energy = artist_energy.head(10)

plt.figure(figsize=(10,5))

top_artist_energy.sort_values().plot(kind='barh')

plt.xlabel('Average Energy')
plt.ylabel('Artist')
plt.title('Top 10 Artists by Average Energy')

plt.tight_layout()

plt.savefig('images/top_10_artists_by_energy.png') 