from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True) #frequent tab closing problem
driver = webdriver.Chrome(options=chrome_options)


driver.get('https://www.amazon.com/') #interacting with browser

#initiate search 
search_bar = driver.find_element(By.ID,'twotabsearchtextbox')

user_input = input('Enter what you want: ')

search_bar.send_keys(f'{user_input}')

search_bar.submit()