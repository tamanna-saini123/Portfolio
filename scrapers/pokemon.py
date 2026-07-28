import requests

def scrape_pokemon_data():

    url = "https://pokeapi.co/api/v2/pokemon?limit=20"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    pokemon_list = []

    for pokemon in data["results"]:

        details = requests.get(pokemon["url"]).json()

        pokemon_list.append({

            "name": details["name"].title(),

            "image": details["sprites"]["other"]["official-artwork"]["front_default"],

            "height": details["height"],

            "weight": details["weight"],

            "types": ", ".join(
                t["type"]["name"].title()
                for t in details["types"]
            )

        })

    return pokemon_list