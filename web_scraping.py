import requests
import os
from time import sleep

def fetch_mvp_data(years, output_dir="mvp"):
    url_start = "https://www.basketball-reference.com/awards/awards_{}.html"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for year in years:
        url = url_start.format(year)
        sleep(5)
        try:
            response = requests.get(url)
            response.raise_for_status()  # Ensure we notice bad responses
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err} - Skipping year {year}")
            sleep(8)  # Adding delay in case of too many requests
            continue
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e} - Skipping year {year}")
            continue

        file_path = os.path.join(output_dir, f"{year}.html")
        with open(file_path, "w+") as f:
            f.write(response.text)
        print(f"Saved data for year {year}")

if __name__ == "__main__":
    years = list(range(1991, 2025))
    fetch_mvp_data(years)