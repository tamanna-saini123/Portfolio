from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

import time



def scrap_booking_data():

    options = Options()

    options.add_argument("--disable-notifications")

    options.add_argument("--disable-popup-blocking")

    # Uncomment if you want background scraping
    # options.add_argument("--headless")


    driver = webdriver.Chrome(options=options)

    driver.maximize_window()


    driver.get("https://www.booking.com/")


    wait = WebDriverWait(driver,20)



    # Close popup if appears

    try:

        close = wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "button[aria-label='Dismiss']"
                )
            )
        )

        close.click()


    except:

        pass



    # Search destination

    try:

        search = wait.until(
            EC.element_to_be_clickable(
                (
                    By.NAME,
                    "ss"
                )
            )
        )


        search.click()

        search.clear()

        search.send_keys("Delhi")


        time.sleep(2)


        search.send_keys(Keys.ENTER)



    except Exception as e:

        print("Search error:",e)

        driver.quit()

        return []



    # Wait for hotels

    try:

        hotels = wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.CSS_SELECTOR,
                    'div[data-testid="property-card"]'
                )
            )
        )


    except:

        driver.quit()

        return []



    data=[]



    for hotel in hotels[:12]:


        try:

            name = hotel.find_element(
                By.CSS_SELECTOR,
                '[data-testid="title"]'
            ).text


        except:

            name="N/A"



        try:

            rating = hotel.find_element(
                By.CSS_SELECTOR,
                '[data-testid="review-score"]'
            ).text


        except:

            rating="N/A"



        try:

            link = hotel.find_element(
                By.TAG_NAME,
                "a"
            ).get_attribute("href")


        except:

            link="N/A"



        try:

            image = hotel.find_element(
                By.TAG_NAME,
                "img"
            ).get_attribute("src")


        except:

            image=""



        data.append({

            "Hotel Name":name,

            "Rating":rating,

            "Hotel Link":link,

            "Image URL":image

        })



    driver.quit()


    return data