from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

import csv
import os
import time

BASE_URL = 'https://www.kabum.com.br/busca/'
LIMIT_DATA_ROWS = None

search = input('Search for: ')

url = BASE_URL + search

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
time.sleep(2)

url_atual = driver.current_url

data = {
    'title': [], 
    'price': [],
    'image': [],
    'url': [],
}

rows = 0

def scraper():
    global rows
    products = driver.find_elements(By.CLASS_NAME, 'productCard')
    for p in products:
        title = p.find_element(By.CLASS_NAME, 'nameCard').text
        price = p.find_element(By.CLASS_NAME, 'priceCard').text
        image = p.find_element(By.TAG_NAME, 'img').get_attribute('src')
        product_url = p.find_element(By.CLASS_NAME, 'productLink').get_attribute('href')

        data['title'].append(title)
        data['price'].append(price)
        data['image'].append(image)
        data['url'].append(product_url)

        rows += 1

        if LIMIT_DATA_ROWS and rows >= LIMIT_DATA_ROWS:
            break

def save(name, data):
    if not os.path.exists('kabum/data'):
        os.makedirs('kabum/data')

    with open(f'kabum/data/{name}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Image URL', 'Product URL'])

        for i in range(len(data['title'])):
            writer.writerow([data['title'][i], data['price'][i], data['image'][i], data['url'][i]])

pagination = driver.find_elements(By.CLASS_NAME, 'pagination')

if pagination:
    pages = pagination[0].find_elements(By.TAG_NAME, 'a')
    total_pages = int(pages[-2].text)
else:
    total_pages = 1

for page in range(1, total_pages + 1):
    if LIMIT_DATA_ROWS and rows >= LIMIT_DATA_ROWS:
        break

    driver.get(url_atual + f'?page_number={page}')
    time.sleep(2)
    scraper()

driver.quit()

save(name=search, data=data)
