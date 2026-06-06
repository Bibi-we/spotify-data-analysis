import pandas as pd 

import matplotlib.pyplot as plt 

df = pd.read_csv('data/tracks.csv')

print(df.head()) # first five rows 

print(df.shape) # number of rows and columns

print(df.columns) # column names 

print(df.dtypes) # data types of each column

print(df.isnull().sum()) # missing values in each column

print(df['popularity'].describe()) # summary statistics for the popularity column 

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
