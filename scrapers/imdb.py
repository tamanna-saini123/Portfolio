from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrap_imdb_data():

    driver = webdriver.Chrome()
    driver.get("https://www.imdb.com/chart/top/")
    time.sleep(5)

    movies = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")

    data = []

    for movie in movies:
        try:
            # Title
            title = movie.find_element(By.CSS_SELECTOR, "h4.ipc-title__text").text

            # Image URL
            image = movie.find_element(By.TAG_NAME, "img").get_attribute("src")

            # Metadata
            metadata = movie.find_elements(By.CSS_SELECTOR, "li.ipc-inline-list__item")

            year = metadata[0].text if len(metadata) > 0 else "N/A"
            duration = metadata[1].text if len(metadata) > 1 else "N/A"
            certificate = metadata[2].text if len(metadata) > 2 else "N/A"

            # Rating
            rating = movie.find_element(
                By.CSS_SELECTOR,
                "span.ipc-rating-star--rating"
            ).text

            data.append({
                "Title": title,
                "Year": year,
                "Duration": duration,
                "Certificate": certificate,
                "Rating": rating,
                "Image URL": image
            })

        except Exception as e:
        
            continue

    driver.quit()
    return data