from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import csv
import os
import time
import threading
import itertools
import sys

class Kabum:
    def __init__(self, search, limit=None):
        self.BASE_URL = 'https://www.kabum.com.br/busca/'
        self.LIMIT_DATA_ROWS = limit
        self.search = search
        self.url = self.BASE_URL + search
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.data = {
            'title': [], 
            'price': [],
            'image': [],
            'url': [],
        }
        self.rows = 0

    def scraper(self):
        products = self.driver.find_elements(By.CLASS_NAME, 'productCard')
        for p in products:
            title = p.find_element(By.CLASS_NAME, 'nameCard').text
            price = p.find_element(By.CLASS_NAME, 'priceCard').text
            image = p.find_element(By.TAG_NAME, 'img').get_attribute('src')
            product_url = p.find_element(By.CLASS_NAME, 'productLink').get_attribute('href')

            self.data['title'].append(title)
            self.data['price'].append(price)
            self.data['image'].append(image)
            self.data['url'].append(product_url)

            self.rows += 1

            if self.LIMIT_DATA_ROWS and self.rows >= self.LIMIT_DATA_ROWS:
                break

    def save(self):
        if not os.path.exists('kabum/data'):
            os.makedirs('kabum/data')

        with open(f'kabum/data/{self.search}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Price', 'Image URL', 'Product URL'])

            for i in range(len(self.data['title'])):
                writer.writerow([self.data['title'][i], self.data['price'][i], self.data['image'][i], self.data['url'][i]])

    def run(self):
        self.driver.get(self.url)
        time.sleep(2)

        url_atual = self.driver.current_url
        pagination = self.driver.find_elements(By.CLASS_NAME, 'pagination')

        if pagination:
            pages = pagination[0].find_elements(By.TAG_NAME, 'a')
            total_pages = int(pages[-2].text)
        else:
            total_pages = 1

        for page in range(1, total_pages + 1):
            if self.LIMIT_DATA_ROWS and self.rows >= self.LIMIT_DATA_ROWS:
                break

            self.driver.get(url_atual + f'?page_number={page}')
            time.sleep(2)
            self.scraper()

        self.driver.quit()
        self.save()

def spinner():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(f'\rLoading... {c}')
        sys.stdout.flush()
        time.sleep(0.1)


if __name__ == "__main__":
    search_term = input("Search for: ")

    done = False
    t = threading.Thread(target=spinner)
    t.start()

    scraper = Kabum(search=search_term, limit=None)
    scraper.run()

    done = True
    t.join()

    sys.stdout.write('\rScraping complete!           \n')
