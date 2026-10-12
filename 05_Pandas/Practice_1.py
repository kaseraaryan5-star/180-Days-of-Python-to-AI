import numpy as np
import pandas as pd

#DataFrame Methods
marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14],
],columns=['iq','marks','package'])

print(marks)

# 1.value_counts(series and dataframe)
a = pd.Series([1,1,1,1,2,2,2,2,23,3,3,3,3,3,3,3,5,55,5,5,5,5,])
print(a.value_counts())

b = marks.value_counts()
print(b)

ipl = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/ipl-matches.csv')
print(ipl.head(2))

#find which player has won most potm -> in finals and qualifiers
print(ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts())

#toss decision plot
print(ipl['TossDecision'].value_counts().plot(kind='pie'))

#how many matches each team has played
print((ipl['Team1'].value_counts() + ipl['Team2'].value_counts()).sort_values(ascending=False))


# 2.sort_values(series and dataframe) -> ascending -> na_position -> inplace -> multiple columns
x = pd.Series([12,77,5,4,3,6,9,99])
print(x.sort_values())
print(x.sort_values(ascending=False))

movies = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/movies.csv')
print(movies)
print(movies.sort_values('title_x',ascending=False))

students = pd.DataFrame(
    {
        'name' : ['nitish','ankit','rupesh',np.nan,'mrtiyunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college' : ['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch' : ['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa' : [6,66,8.25,6.41,np.nan,5.6,9.0,7.4,10,np.nan],
        'package' : [4,5,6,np.nan,6,7,8,9,np.nan,np.nan]
    }
)
print(students)
print(students.sort_values('branch',ascending=False,inplace=True))

print(movies.sort_values(['year_of_release','title_x']))


# 3.rank(series)
batsman = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/batsman_runs_ipl.csv')
print(batsman) 

batsman = batsman.rank(ascending=False)
print(batsman)

batsman['batting_rank'] = batsman['batsman_run'].rank(ascending=False)
print(batsman.sort_values('batting_rank'))


# 4.sort_index(series and dataframe)
marks = {
    'maths' : 67,
    'english' : 57,
    'hindi' : 100,
    'science' : 88
}
marks_series = pd.Series(marks)
print(marks_series)

print(marks_series.sort_index)

print(movies.sort_index(ascending=False))


# 5.set_index(dataframe) -> inplace
print(batsman)
print(batsman.set_index('batter',inplace=True))


# 6.reset_index(series and dataframe) -> drop parameter
print(batsman.reset_index(inplace=True))

#how to replace existing index without loosing
print(batsman.reset_index().set_index('batting_rank'))


#series to dataframe using reset_index
print(marks_series.reset_index())


# 7.rename(dataframe)   (changes name of index and columns as pr required)
print(movies.set_index('title_x',inplace=True))
print(movies)

print(movies.rename(columns={'imdb_id':'imdb','poster_path':'link'}))
print(movies.rename(index={'Uri: The Surgical Strike':'URI','Battalion 609':'Battalion'}))


# 8.unique(series)    (counts nun number also)
temp = pd.Series([12,3,4,5,3,3,4,3,7,8,9,65,4,5,6,677,])
print(temp.unique())


# 9.isnull(series and dataframe)
print(students['name'].isnull())
print(students.isnull())


# 10.notnull(series and dataframe)
print(students['name'].notnull())
print(students.notnull())


# 11.hasnans(series)
print(students['name'].hasnans)


# 12.dropna(series and dataframe) -> how parameter -> works like or
print(students)
print(students['name'].dropna())
print(students.dropna())

print(students.dropna(how='all'))
print(students.dropna(subset=['name']))
print(students.dropna(subset=['name','college']))


# 13.fillna(series and dataframe)
print(students)
print(students['name'].fillna('unknown'))
print(students['package'].fillna(students['package'].mean()))


# 14.drop_duplicates(series and dataframe) -> works like and -> duplicated()
temp = pd.Series([1,1,2,3,2,1,3,4,5,6,43,3,2,43,5,6,7])
print(temp.drop_duplicates())

marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14],
],columns=['iq','marks','package'])

print(marks)
print(marks.drop_duplicates())

#find the last match played by virat kohli in Delhi
print(ipl)
ipl['all_players'] = ipl['Team1Players'] + ipl['Team2Players']
print('all_players')
print(ipl.head())
def did_kohli_play(players_list):
    return 'V Kohli' in players_list

ipl['did_kohli_play'] = ipl['all_players'].apply(did_kohli_play)
ipl_filtered = ipl[(ipl['City'] == 'Delhi') & (ipl['did_kohli_play'] == True)]
print(ipl_filtered.drop_duplicates(subset=['City','did_kohli_play']))



# 15.drop(series and dataframe)
temp = pd.Series([10,4,3,2,5,6,7,8,9,0,4,5,6])
print(temp)
print(temp.drop([0,6]))

print(students)
print(students.drop(columns=['branch','cgpa']))
print(students.drop(index=[0,8]))



# 16.apply(series and dataframe)
temp = pd.Series([10,20,30,40,50])
print(temp)

def sigmoid(value):
    return 1/1+np.exp(-value)
print(temp.apply(sigmoid))

points_df = pd.DataFrame(
    {
        '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
        '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
    }
)
print(points_df)

def euclidean(row):
    pt_A = row['1st point']
    pt_B = row['2nd point']

    return ((pt_A[0] - pt_B[0])**2 + (pt_A[1] - pt_B[1])**2)**0.5
points_df['distance'] = points_df.apply(euclidean,axis=1)
print(points_df)