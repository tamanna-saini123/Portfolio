import requests

def scrape_jikan_data():

    url = "https://api.jikan.moe/v4/top/anime"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    anime_list = []

    for anime in data.get("data", []):

        anime_list.append({

            "title": anime.get("title", "N/A"),
            "score": anime.get("score", "N/A"),
            "episodes": anime.get("episodes", "Unknown"),
            "status": anime.get("status", "Unknown"),
            "year": anime.get("year", "N/A"),
            "image": anime.get("images", {}).get("jpg", {}).get("image_url", "")

        })

    return anime_list