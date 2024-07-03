# First Run
import requests
import os
import time
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

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

# Second Run: Process the downloaded HTML files
dfs = []
for year in years:
    try:
        with open(f"mvp/{year}.html", encoding='utf-8') as f:
            page = f.read()
        soup = BeautifulSoup(page, "html.parser")
        
        # Check if 'over_header' exists and remove it if it does
        over_header = soup.find('tr', class_="over_header")
        if over_header:
            over_header.decompose()
        
        # Find the MVP table
        mvp_table = soup.find('table', id="mvp")
        if not mvp_table:
            print(f"No MVP table found for the year {year}")
            continue
        
        # Convert the MVP row to a DataFrame
        mvp = pd.read_html(StringIO(str(mvp_table)))[0]
        dfs.append(mvp)
    except FileNotFoundError:
        print(f"File not found for the year {year}")
    except Exception as e:
        print(f"Error processing data for the year {year}: {e}")

mvps = pd.concat(dfs)
mvps.tail()
mvps.to_csv("mvp.csv")