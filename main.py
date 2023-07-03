import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os

# Set headers for HTTP requests:
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

# URLs for each platform
urls = {
    'tiktok': 'https://en.wikipedia.org/wiki/List_of_most-followed_TikTok_accounts',
    'youtube': 'https://en.wikipedia.org/wiki/List_of_most-subscribed_YouTube_channels',
    'instagram': 'https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts',
    'twitter': 'https://en.wikipedia.org/wiki/List_of_most-followed_Twitter_accounts'
}

# Function to scrape data from a Wikipedia page
def scrape_wikipedia(url, platform):
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.content, 'html5lib')

    table = soup.find("table", {"class": "wikitable sortable"})

    trs = table.find_all("tr")
    zero_row = trs[0].find_all("th")
    columns = []
    for i in range(len(zero_row)):
        columns.append(zero_row[i].text.strip())

    rows = []
    for i in range(1, 51):
        ith_row = trs[i].find_all("td")
        row = []
        row.append(i)
        for i in range(len(ith_row)):
            row.append(ith_row[i].text.strip())
        rows.append(row)

    df = pd.DataFrame(rows, columns=columns)
    if "Brandaccount" in columns:
        df.drop(["Brandaccount"], axis=1, inplace=True)

    now = datetime.datetime.now()
    filename = f"{now.strftime('%Y-%m')}/{platform}_top_50_{now.strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)

    return filename

# Scrape data for each platform
for platform, url in urls.items():
    filename = scrape_wikipedia(url, platform)
    print(f"Scraped data for {platform} and saved to {filename}")
