import numpy as np
import pandas as pd

movies = pd.read_csv("05_Pandas/movies.csv")
print(movies)
ipl = pd.read_csv("05_Pandas/ipl-matches.csv")
print(ipl)

#Selecting columns from a DataFrame
#one column
print(movies["title_x"])
print(ipl["Venue"])

#multiple columns
print(movies[["title_x","year_of_release","actors"]])
print(ipl[["Team1","Team2","WinningTeam"]])



student_dict = {
    "name":["nitish","ankit","rupesh","rishabh","amit","ankita"],
    "iq":[100,90,120,80,70,60],
    "marks":[80,70,100,50,90,60],
    "package":[10,7,14,5,9,8],
}
students = pd.DataFrame(student_dict)
students.set_index("name",inplace=True)
print(students)

#Selecting rows from a DataFrame
# 1. iloc - searches using index positions   (last value not included)
# 2. loc - searches using index labels       (last value included)

# 1.iloc
#single row
print(movies.iloc[0])
print(ipl.iloc[5])

#multiple rows
print(movies.iloc[0:6])
print(ipl.iloc[0:11:2])

#fancy indexing 
print(movies.iloc[[0,5,1600]])
print(ipl.iloc[[3,56,79,99]])


# 2.loc
print(students.loc["nitish"])
print(students.loc["nitish":"amit"])



#Selecting rows and columns
print(movies.iloc[0:3,0:3])
print(movies.loc[0:2,"title_x":"poster_path"])



#Filtering a DataFrame
print(ipl)
print(movies)

#find all the final winners
mask = ipl["MatchNumber"]== "Final"
new_df = ipl[mask]
print(new_df[['Season','WinningTeam']])

print(ipl[ipl['MatchNumber']=='Final'][['Season','WinningTeam']])

#how many super over finishes have occured
print(ipl[ipl['SuperOver']=='Y'].shape[0])

#how many matches has csk won in Kolkata
print(ipl[(ipl['City']=='Kolkata')&(ipl['WinningTeam']=='Chennai Super Kings')].shape[0])

#toss winner is match winner in percentage
print(ipl[ipl['TossWinner']==ipl['WinningTeam']].shape[0]/ipl.shape[0]*100)

#movies with rating higher than 8 and votes>10000
print(movies[(movies['imdb_rating'] > 8)&(movies['imdb_votes'] > 10000)].shape[0])

#action movies with rating higher than 7.5
mask1 = movies['genres'].str.split('|').apply(lambda x:'Action' in x)
mask2 = movies['imdb_rating'] > 7.5

print(movies[mask1 & mask2].shape[0])



#Adding new columns
#completely new
movies['Country'] = 'India' 
print(movies.head())

#from existing ones
movies['lead actor'] = movies['actors'].str.split('|').apply(lambda x:x[0])
print(movies.head())



#Important DataFrame Functions
#astype
print(ipl.info())
ipl['ID'] = ipl['ID'].astype('int32')
print(ipl['ID'])
print(ipl.info())
