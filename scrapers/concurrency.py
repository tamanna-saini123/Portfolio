import requests
import pandas as pd

def scrape_concurrency_data():

    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"

    response = requests.get(url)

    data = response.json()

    coins = []

    for coin in data:
        coins.append({
            "Name": coin["name"],
            "Symbol": coin["symbol"].upper(),
            "Price (USD)": coin["current_price"],
            "Market Cap": coin["market_cap"],
            "Rank": coin["market_cap_rank"]
        })

    return coins