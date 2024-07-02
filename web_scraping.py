import requests
import os
import time
from bs4 import BeautifulSoup
import pandas as pd

# Define the years range
years = list(range(1991, 2025))
url_start = "https://www.basketball-reference.com/awards/awards_{}.html"

# Create directory if it doesn't exist
if not os.path.exists("mvp"):
    os.makedirs("mvp")

# First Run: Download HTML files with delay and error handling
for year in years:
    url = url_start.format(year)
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        if response.status_code == 200:
            with open("mvp/{}.html".format(year), "w+", encoding='utf-8') as f:
                f.write(response.text)
            print(f"Successfully fetched data for {year}")
        else:
            print(f"Failed to fetch data for {year}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {year}: {e}")
    
    time.sleep(20)  # Delay to prevent rate limiting

