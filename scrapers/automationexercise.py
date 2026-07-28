from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrap_automationexercise_data():

    driver = webdriver.Chrome()

    driver.get("https://automationexercise.com/products")
    time.sleep(5)

    products = driver.find_elements(By.CLASS_NAME, "product-image-wrapper")

    data = []

    for product in products:

        try:
            name = product.find_element(By.TAG_NAME, "p").text
        except:
            name = "N/A"

        try:
            price = product.find_element(By.TAG_NAME, "h2").text
        except:
            price = "N/A"

        try:
            image = product.find_element(By.TAG_NAME, "img").get_attribute("src")
        except:
            image = ""

        data.append({
            "Product": name,
            "Price": price,
            "Image URL": image
        })

    driver.quit()

    return data