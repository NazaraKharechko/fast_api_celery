from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json

url = 'https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html'
res = []

class SpanScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        time.sleep(4)

        # # Плавна прокрутка сторінки до самого низу
        # scroll_pause_time = 0.2   # Час затримки між прокрутками (можна налаштувати)
        # scroll_height_step = 1000  # Кількість пікселів для прокрутки за один крок
        #
        # last_height = driver.execute_script("return document.body.scrollHeight")
        #
        # while True:
        #     # Прокручуємо сторінку вниз на невеликий крок
        #     driver.execute_script(f"window.scrollBy(0, {scroll_height_step});")
        #     time.sleep(scroll_pause_time)
        #
        #     # Оновлюємо висоту сторінки після прокрутки
        #     new_height = driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height

        # Отримати HTML-код сторінки
        html_code = driver.page_source
        soup = BeautifulSoup(html_code, 'html.parser')

        # Знайти всі теги 'a' з класом 'result-item-heading' і пропустити перші 20 в посиланні
        span_elements = soup.find_all('a', {'class': 'cmp-category__item-link'})
        spans_href = [span.get('href') for span in span_elements]
        for i in spans_href:
            res.append('https://www.mcdonalds.com/' + i)
        print(len(res))
        print(res)
        driver.quit()

        # Запис в файл всіх посилань на менб мака
        # with open('links.json', 'w') as f:
        #     json.dump(res, f)
        return spans_href


if __name__ == "__main__":
    scraper = SpanScraper(url)
    spans_text = scraper.scrape()

