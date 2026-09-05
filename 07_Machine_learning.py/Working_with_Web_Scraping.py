import pandas as pd
import requests
from bs4 import BeautifulSoup

# हेडर जो ब्राउज़र जैसा रिस्पांस दिखाता है
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
}

# 1. वेबसाइट से डेटा मंगाना
response = requests.get('https://www.ambitionbox.com/list-of-companies?page=1', headers=headers)

# 2. BeautifulSoup की मदद से HTML पार्स करना
soup = BeautifulSoup(response.text, 'lxml')

# 3. नए स्ट्रक्चर के हिसाब से कंपनी के मुख्य कार्ड्स को ढूँढना
company = soup.find_all('div', class_='companyCardWrapper')

print(f"Total Companies Found: {len(company)}")
print("-" * 50)

# 4. सभी कंपनियों का नाम, रेटिंग और रिव्यू निकालना
for c in company:
    # कंपनी का नाम निकालना
    name_tag = c.find('h2', class_='companyCardWrapper__companyName')
    name = name_tag.text.strip() if name_tag else "N/A"
    
    # कंपनी की रेटिंग निकालना
    rating_tag = c.find('span', class_='companyCardWrapper__companyRatingNumber')
    rating = rating_tag.text.strip() if rating_tag else "N/A"
    
    # कंपनी के टोटल रिव्यू निकालना
    reviews_tag = c.find('span', class_='companyCardWrapper__ActionCount')
    reviews = reviews_tag.text.strip() if reviews_tag else "N/A"
    
    # टर्मिनल में डेटा प्रिंट करना
    print(f"Company: {name}")
    print(f"Rating: {rating}")
    print(f"Reviews: {reviews}")
    print("-" * 50)