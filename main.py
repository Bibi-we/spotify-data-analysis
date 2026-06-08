import pandas as pd 

import matplotlib.pyplot as plt 

df = pd.read_csv('data/tracks.csv')

print(df.head()) # first five rows 

print(df.shape) # number of rows and columns

print(df.columns) # column names 

print(df.dtypes) # data types of each column

print(df.isnull().sum()) # missing values in each column

# exploring the data further 
print(df['popularity'].describe()) # summary statistics for the popularity column
print(df[["danceability"]].describe()) # detailed statistics for danceability only
print(df[["energy"]].describe()) # detailed statistics for energy only
print(df[["tempo"]].describe()) # detailed statistics for tempo only


top_songs = df[['name', 'popularity']].sort_values(by='popularity', ascending=False) # top songs by popularity
print(top_songs.head(10)) # display top 10 popular songs

# visualize the top 10 popular song 

top_10  = top_songs.head(10)

plt.figure(figsize=(10,5))
plt.barh(top_10['name'], top_10['popularity'])
plt.xlabel('popularity')
plt.title('top 10 popular songs')
plt.tight_layout()

plt.savefig('images/top_10_songs.png') # save the figure png 

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