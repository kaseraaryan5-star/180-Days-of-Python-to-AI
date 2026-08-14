import numpy as np
import pandas as pd

movies = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/imdb-top-1000.csv')
print(movies)

# genres = movies.groupby('Genre')
# print(genres)
# print(movies)

# # applying builtin aggregation functions on groupby objects
# print(genres.sum())
# print(genres.min())
# print(genres.max())
# print(genres.mean)
# print(genres.median)
# print(genres.std)
# print(genres.var)

# #find the top 3 genres by total earning
# print(movies.groupby('Genre').sum()['Gross'].sort_values(ascending=False).head(3))
# print(movies.groupby('Genre')['Gross'].sum().sort_values(ascending=False).head(3))

# #find the genre with highest avg IMDB rating
# print(movies.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(1))

# #find director with most popularity
# print(movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1))

# #find number of movies done by each actor
# print(movies.groupby('Star1')['Series_Title'].count().sort_values(ascending=False))



# # GroupBy Attributes and Methods
genre = movies.groupby('Genre')
# print(genre)

# #find total number of groups ->len
# print(len(genre))
# print(genre.nunique())

# #find items in each group -> size
# print(genre.size())
# print(genre.value_counts())

# #first()/last() -> nth item
# print(genre.first())
# print(genre.last())
# print(genre.nth(6))

# #get_group -> vs filtering
# print(genre.get_group('Action'))
# print(genre.get_group('Fantasy'))

# #groups
# print(genre.groups)

# #describe
# print(genre.describe())

# #sample
# print(genre.sample())

# #nunique
# print(genre.nunique)



# #Arregrate Method
# #passing dict
# genre.agg(
#     {
#         'Runtime':'mean',
#         'IMDB_Rating':'mean',
#         'No_of_Votes':'sum',
#         'Gross':'sum',
#         'Metascore':'min'
#     }
# )
# print(genre.agg)

# #passing list
# print(genres.agg(['min','max','sum']))

# #adding both the syntax
# genres.agg(
#     {
#         'Runtime':['min','mean'],
#         'IMDB_Rating':'mean',
#         'No_of_Votes':['sum','max'],
#         'Gross':'sum',
#         'Metascore':'min'
#     }
# )
# print(genres.agg)



# #looping on groups
# dff = pd.DataFrame(columns=movies.columns)
# for group,data in genres:
#     dff = pd.concat([dff, data[data['IMDB_Rating'] == data['IMDB_Rating'].max()]],ignore_index=True)

# print(dff)



#Split-(apply)-combine method
#apply -> builtin function
print(genre.apply(min))

#find number of movies starting with A for each group
def foo(group):
    return group['Series_Title'].str.startswith('A').sum()
print(genre.apply(foo))

#find rank of each movie in the group according to IMDB score
def rank_movie(group):
    group['genre_rank'] = group['IMDB_Rating'].rank(ascending=False)
    return group
print(genre.apply(rank_movie))

#find normalized IMDB rating group wise
def normal(group):
    group['Normalized_IMDB_rating'] == (group['IMDB_Rating'] - group['IMDB_Rating'].min())/(group['IMDB_Rating'].max() - group['IMDB_Rating'].min())
    return group
print(genre.apply(normal))