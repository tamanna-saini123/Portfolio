from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrap_spotify_data():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")   # Runs Chrome in the background
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    driver.get("https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF")
    time.sleep(5)

    rows = driver.find_elements(
        By.CSS_SELECTOR,
        "div[data-testid='tracklist-row']"
    )

    data = []

    for row in rows:

        try:
            song = row.find_element(
                By.CSS_SELECTOR,
                "a[href*='/track/']"
            ).text
        except:
            song = "N/A"

        try:
            artist = row.find_element(
                By.CSS_SELECTOR,
                "span a[href*='/artist/']"
            ).text
        except:
            artist = "N/A"

        try:
            duration = row.find_element(
                By.CSS_SELECTOR,
                "div[aria-colindex='5']"
            ).text
        except:
            duration = "N/A"

        data.append({
            "Song": song,
            "Artist": artist,
            "Duration": duration
        })

    driver.quit()

    return data