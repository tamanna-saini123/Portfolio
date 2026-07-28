from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://finance.yahoo.com/markets/currencies/"


headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrap_finance_data():

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser' )
    soup.prettify()

    yahoo_finance = soup.find_all("div",class_	='tableContainer yf-1nql2a7')

    data=[]

    rows = soup.find_all("tr")
    for row in rows:
    # Extract all columns (cells) in the row
        cols = row.find_all("td")
    # Append the cleaned text values into data list
        data.append([col.get_text(strip=True) for col in cols])

    return data