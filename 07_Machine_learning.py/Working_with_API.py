import time
import pandas as pd
import requests

temp_df = pd.DataFrame()
session = requests.Session()  # Yeh connection ko stable rakhega

for i in range(1, 63):
  url = f"https://api.themoviedb.org/3/keyword/9715/movies?api_key=77ec7a7e2c70a54dc1c76ea977459b2b&page={i}"

  try:
    response = session.get(url, timeout=10)

    if response.status_code == 200:
      data = response.json()
      if "results" in data and len(data["results"]) > 0:
        df_page = pd.DataFrame(data["results"])[
            ["id", "title", "release_date", "overview", "popularity"]
        ]
        temp_df = pd.concat([temp_df, df_page], ignore_index=True)
      else:
        print(f"Data khatam ho gaya page {i} par.")
        break
    else:
      print(f"Page {i} par error aaya: Status {response.status_code}")

  except requests.exceptions.RequestException:
    # Agar error aaye bhi toh chupचाप agle page par move ho jaye
    time.sleep(1)
    continue

  # Server par load na pade isiliye chota sa gap
  time.sleep(0.5)

print("Total rows collected:", len(temp_df))

temp_df.to_csv('movies_data.csv', index=False)
print("File successfully save ho gayi hai!")

df = pd.read_csv('/Users/aryankasera/Desktop/100-Days-AI/movies_data.csv')
print(df)