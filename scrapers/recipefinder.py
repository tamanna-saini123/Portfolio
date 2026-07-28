import requests

def scrape_recipe_data():

    meal = "chicken"

    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal}"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    recipes = []

    if data.get("meals"):

        for item in data["meals"]:

            recipes.append({

                "meal": item.get("strMeal"),

                "category": item.get("strCategory"),

                "cuisine": item.get("strArea"),

                "instructions": item.get("strInstructions", "")[:150] + "...",

                "image": item.get("strMealThumb"),

                "youtube": item.get("strYoutube")

            })

    return recipes