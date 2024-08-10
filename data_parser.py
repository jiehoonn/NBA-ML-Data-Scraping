from bs4 import BeautifulSoup
import os
import pandas as pd

def parse_mvp_data(year, input_dir="mvp", output_dir="output"):
    file_path = os.path.join(input_dir, f"{year}.html")
    if not os.path.exists(file_path):
        print(f"File for year {year} not found.")
        return None
    
    with open(file_path, "r") as f:
        page = f.read()
    
    soup = BeautifulSoup(page, 'html.parser')
    if soup.find('tr', class_="over_header"):
        soup.find('tr', class_="over_header").decompose()

    mvp_table = soup.find('table', {"id": "mvp"})
    
    if mvp_table:
        print(f"MVP table found for year {year}")
        rows = mvp_table.find_all('tr')
        data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Save DataFrame to CSV
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        df.to_csv(os.path.join(output_dir, f"mvp_{year}.csv"), index=False)
        print(f"Data for year {year} saved to {output_dir}/mvp_{year}.csv")
        return df
    else:
        print(f"MVP table not found for year {year}")
        return None

if __name__ == "__main__":
    years = list(range(1991, 2025))
    for year in years:
        parse_mvp_data(year)