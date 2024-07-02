# First Run
import requests

years = list(range(1991, 2025))
url_start = "https://www.basketball-reference.com/awards/awards_{}/html" # {} allows us to flexibly scrape the data of a certain year

for year in years:
    url = url_start.format(year)
    data = requests.get(url)

    with open("mvp/{}.html".format(year), "w+") as f:
        f.write(data.text)

