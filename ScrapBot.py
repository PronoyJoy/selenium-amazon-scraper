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

def scraping(product):  # sourcery skip: do-not-use-bare-except

   try:
        h2 = product.h2
   except:
       title =''
       url = ''
   else:
       title = h2.text.strip()
       url = h2.a.get('href')

   try:
      rating = product.find('span',class_ ='a-icon-alt').text
   except Exception:
      rating =''

   try:
      price = product.find('span',class_ ='a-price-whole').text
   except Exception:
      price = ''
   else:
      price = ''.join(price.split(','))

   data = {'title' : title, 'rating' : rating, 'price':price, 'url':url}

   return data
       
       
       

   
   
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

   products = soup.find_all('div', {'data-asin': True, 'data-component-type' : 's-search-result'})
    
   product_dict = []
   for product in products:
      product_dict.append(product)

first_bot()