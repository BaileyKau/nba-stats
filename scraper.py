import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def get_dynamic_html(url):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)

        input("Please log in manually, and then press Enter to continue...")
        driver.get(url)

        time.sleep(5)

        dynamic_html = driver.page_source

    finally:
        driver.quit()

    return dynamic_html

def fetch_data(html):
    output = ""
    soup = BeautifulSoup(html,'html.parser')

    player_elements = soup.findAll(class_ = "styles__overUnderCell__KgzNn")    


    for player_element in player_elements:
        player_name = player_element.find(class_ = "styles__playerName__jW6mb")
        name = player_name.get_text()
        output += f"{name}:\n"

        player_lines = player_element.findAll(class_ = "styles__statLine__K1NYh")

        for player_line in player_lines:
            line = player_line.get_text()
            output+= f"{line} | "
        
        output+="\n\n"

    return output

def main():
    url = "https://underdogfantasy.com/pick-em/higher-lower/all/nba"
    dynamic_html = get_dynamic_html(url)
    data = fetch_data(dynamic_html)
    print(data)


main()



