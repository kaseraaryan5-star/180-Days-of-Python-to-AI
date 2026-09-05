import pandas as pd
import requests

response = requests.get('https://api.themoviedb.org/3/keyword/9715/movies?api_key=77ec7a7e2c70a54dc1c76ea977459b2b')
print(response)
print(response.json()['results'])

df = pd.DataFrame(response.json()['results'])[['id','title','release_date','overview','popularity','vote_average','vote_count']]
print(df)
print(df.head())

for i in range(1,63):
    response = requests.get('https://api.themoviedb.org/3/keyword/9715/movies?api_key=77ec7a7e2c70a54dc1c76ea977459b2b.format(i)')
    temp_df = pd.DataFrame(response.json()['results'])[['id','title','release_date','overview','popularity','vote_average','vote_count']]
    df = df.append(temp_df, ignore_index=True)    

print(df)