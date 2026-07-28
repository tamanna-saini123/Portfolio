import requests

def scrape_products_data():

    url = "https://dummyjson.com/products"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    products = []

    for item in data.get("products", []):

        products.append({

            "title": item.get("title", "N/A"),
            "brand": item.get("brand", "N/A"),
            "category": item.get("category", "N/A"),
            "price": item.get("price", 0),
            "rating": item.get("rating", "N/A"),
            "stock": item.get("stock", "N/A"),
            "thumbnail": item.get("thumbnail", "")

        })

    return products