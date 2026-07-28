from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

url = "https://www.goodreads.com/quotes"

headers = {
    'User-Agent' :'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

}

def scrap_quotes_data():

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser' )
    soup.prettify()
    Mydata = soup.find_all("div", class_ ='quote')
    Fetch_data=[]
    Mydata[0].prettify()

    for info in Mydata:
        text = info.find("div", class_="quoteText").get_text(strip=True)
        author = info.find("span", class_="authorOrTitle").get_text(strip=True)
        likes = info.find("a", class_="smallText").get_text(strip=True)
        tags = info.find("div", class_="greyText").get_text(strip=True) if info.find("div", class_="greyText") else None
        image = info.find("img")
        image_url = image["src"] if image else None
   
        Fetch_data.append({
        "quote": text,
        "author": author,
        "likes": likes,
        "tags": tags,
        "image": image_url
        
        })

    return Fetch_data