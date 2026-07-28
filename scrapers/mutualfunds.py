from bs4 import BeautifulSoup
import requests

url = "https://finance.yahoo.com/markets/mutualfunds/top/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def scrap_mutualfund_data():

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    data = []

    rows = soup.find_all("tr")

    for row in rows:
        cols = row.find_all("td")

        if cols:
            data.append([col.get_text(strip=True) for col in cols])

    return data