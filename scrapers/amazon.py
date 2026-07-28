from bs4 import BeautifulSoup
import pandas as pd 
import requests 

url = "https://www.amazon.in/s?k=laptop&crid=YLH7SZQM1WE6&sprefix=laptop%2Caps%2C610&ref=nb_sb_noss_2"

headers = { 'User-Agent' :'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36' } 

def scrap_amazon_data():
    response = requests.get(url, headers=headers)  

    soup = BeautifulSoup(response.content, 'html.parser' ) 

    soup.prettify()

    Amazon = soup.find_all("div", {"data-component-type": "s-search-result"}) 
    Amazon_data = [] 

    for product in Amazon:

        #title = product.find("h2", class_="a-size-large a-spacing-none")
        title = product.find("h2", class_="a-size-medium")
        price = product.find("span", class_="a-price-whole")
        mrp = product.find("span", class_="a-text-price")
        discount = product.find("span", class_="a-letter-space")
        rating = product.find("span", class_="a-icon-alt")
        reviews = product.find("span", class_="a-size-base")


        Amazon_data.append({
        "title": title.text.strip() if title else None,
        "price": price.text if price else None,
        "mrp": mrp.text if mrp else None,
        "discount": discount.text if discount else None,
        "rating": rating.text if rating else None,
        "reviews": reviews.text if reviews else None
        })
        

    return Amazon_data

