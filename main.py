import requests
import json
import time

HEADERS = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "content-type": "application/json",
    "accept-language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7,ru-RU;q=0.6,ru;q=0.5",
    "accept-encoding": "gzip, deflate, br"
}

url = "https://www.zillow.com/homes/New-York,-NY_rb/"

searched_url = """https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.54443904394532%2C%22east%22%3A-73.41147395605469%2C%22south%22%3A40.316985010504276%2C%22north%22%3A41.092563338996484%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3A1%7D%2C%22isPreMarketForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForRent%22%3A%7B%22value%22%3Atrue%7D%2C%22isForSaleByOwner%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isPreMarketPreForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22,%22mapResults%22]}&requestId=4"""

response = requests.get(searched_url,headers=HEADERS)

json_data = response.json()


    # if i["address"] == "--":
    #     print("no address given")
    # else:
    #     print(i["address"])
    
    # print(i["price"])
    # print(i["imgSrc"])
    

docs_url = "https://docs.google.com/forms/d/e/1FAIpQLSf2yUl38T8oyIcqUfYBqBjGBl5TSRcIvGjTManip9T4MOJQwQ/viewform?usp=sf_link"
    
DRIVER_PATH = "C:/Users/evgenyber/Desktop/python studies/chromedriver.exe"
SITE_URL = "https://www.zillow.com"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(DRIVER_PATH)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf2yUl38T8oyIcqUfYBqBjGBl5TSRcIvGjTManip9T4MOJQwQ/viewform")
driver.maximize_window()

time.sleep(1)

for i in json_data["cat1"]["searchResults"]["mapResults"]:
    if i["address"] == "--":
        address_elem = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_elem.send_keys("no address given")
        address_elem.send_keys(Keys.RETURN)
    else:
        address_elem = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_elem.send_keys(i["address"])
        address_elem.send_keys(Keys.RETURN)


    price_elem = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_elem.send_keys(i["price"])
    price_elem.send_keys(Keys.RETURN)

    link_elem = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_elem.send_keys(SITE_URL+i["detailUrl"])
    link_elem.send_keys(Keys.RETURN)

    send_elem = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
    send_elem.click()

    time.sleep(0.2)

    send_again_click = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    send_again_click.click()
    time.sleep(0.2)

driver.close




