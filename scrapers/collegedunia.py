from bs4 import BeautifulSoup
import pandas as pd
import requests

url = ("https://collegedunia.com/")
headers = {
    'User-Agent' :'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

}
def scrap_college_data():

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    soup.prettify()
    data= soup.find_all("tr", class_="jsx-831255015")

    College_data = []

    for i in data:
        College = i.find("div", class_="jsx-831255015 text-dark college-name")
        Ranking = i.find("span", class_="jsx-831255015")
        Cutoff = i.find("div", class_="jsx-831255015 cutoff text-dark")
        Application_Deadline = i.find("div", class_="jsx-831255015 date")
        Fees = i.find("div", class_="jsx-831255015 fees text-dark")

        College_data.append({
        "College": College.get_text(strip=True) if College else "N/A",
        "Ranking": Ranking.get_text(strip=True) if Ranking else "N/A",
        "Cutoff": Cutoff.get_text(strip=True) if Cutoff else "N/A",
        "Application_Deadline": Application_Deadline.get_text(strip=True) if Application_Deadline else "N/A",
        "Fees": Fees.get_text(strip=True) if Fees else "N/A"
    })
    return College_data
