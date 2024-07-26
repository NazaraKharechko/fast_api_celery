import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://realtylink.org/en/apartment~for-sale~duncan/953940?view=Summary&uc=9'


class PropertyScraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def scrape(self):
        results = []
        for _ in range(10):  # Проводимо цикл 60 разів
            self.driver.get(self.url)
            time.sleep(2)  # Затримка, щоб дочекатися завантаження сторінки

            html_code = self.driver.page_source
            soup = BeautifulSoup(html_code, 'html.parser')

            result = {}  # Створюємо новий словник для збереження даних кожної сторінки

            title_advertisement_element = soup.find('div', {'class': 'col text-left pl-0'})
            if title_advertisement_element:
                title_advertisement = title_advertisement_element.text[2:20]
                result['title_advertisement'] = title_advertisement
            else:
                print('Title advertisement element not found')

            region_element = soup.find('h2', {'class': 'pt-1'})
            if region_element:
                region = region_element.text[70:-1]
                result['region'] = region
            else:
                print('Region element not found')

            address_element = soup.find('h2', {'class': 'pt-1'})
            if address_element:
                address = address_element.text[49:-1]
                result['address'] = address
            else:
                print('Address element not found')

            price_element = soup.find('div', {'class': 'price text-right'})
            if price_element:
                price = price_element.text[4:]
                result['price'] = price
            else:
                print('Price element not found')

            area_element = soup.find('div', {'class': 'carac-value'})
            if area_element:
                area = area_element.text[20:40]
                result['area'] = area
            else:
                print('Area element not found')

            description_element = soup.find('div', {'class': 'property-description col-md-12'})
            if description_element:
                description = description_element.text[60:]
                result['description'] = description
            else:
                print('Description element not found')

            # Знайти всі елементи з атрибутом src
            src_elements = soup.find_all(src=True)[24:29]

            # Вивести значення атрибута src для знайдених елементів
            list_src_elements = []
            for element in src_elements:
                list_src_elements.append(element['src'])

            result['url_foto'] = list_src_elements

            # Клікнути на елемент з класом "next"
            show_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//li[@class="next"]')))
            show_button.click()
            time.sleep(2)  # Затримка після кліку

            # Оновити значення змінної url для наступної сторінки
            self.url = self.driver.current_url

            # Додати результат до списку результатів
            results.append(result)
            print(result)

        self.driver.quit()
        return results


class PropertyPrinter:
    @staticmethod
    def print_results(results):
        print(json.dumps(results, indent=4))


if __name__ == "__main__":
    scraper = PropertyScraper(url)
    results = scraper.scrape()
    PropertyPrinter.print_results(results)
