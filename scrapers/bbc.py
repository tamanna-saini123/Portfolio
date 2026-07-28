from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrap_bbc_data():

    driver = webdriver.Chrome()

    driver.get("https://www.bbc.com/news")
    time.sleep(5)

    headlines = driver.find_elements(By.CSS_SELECTOR, "h2, h3")

    data = []

    for headline in headlines:
        try:
            text = headline.text.strip()

            if text:
                data.append({
                    "Headline": text
                })

        except Exception:
            continue

    driver.quit()

    return data
