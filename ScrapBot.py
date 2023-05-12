from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


chrome_options = Options()
chrome_options.add_experimental_option("detach", True) #frequent tab closing problem
driver = webdriver.Chrome(options=chrome_options)


def first_bot():

    driver.get('https://www.amazon.com/') #interacting with browser

   #initiate search 
    search_bar = driver.find_element(By.ID,'twotabsearchtextbox')

    user_input = input('Enter what you want: ')

    search_bar.send_keys(f'{user_input}')
    search_bar.send_keys(Keys.RETURN)

    driver.implicitly_wait(10)

   # retrieve the HTML content after submitting the search query
    html = driver.page_source

    soup = BeautifulSoup(html,'lxml')

    cards = soup.find_all('div', {'data-asin': True, 'data-component-type' : 's-search-result'})

    print(len(cards))

first_bot()