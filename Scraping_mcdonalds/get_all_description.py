import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

# Зчитування посилань із файлу
with open('links.json', 'r') as f:
    all_url = json.load(f)

# Обробка кожної URL по черзі
def scrape():
    # Ініціалізація драйвера
    driver = webdriver.Chrome()

    # Список для зберігання зібраних даних
    all_data = []

    # Цикли для обробки перших
    for url in all_url[:2]:
        print(f"Processing: {url}")
        driver.get(url)
        time.sleep(4)  # Можна замінити на WebDriverWait, але тут чекаємо 4 секунди

        # Отримати HTML-код сторінки
        html_code = driver.page_source
        soup = BeautifulSoup(html_code, 'html.parser')

        try:
            # Витягнення даних з HTML
            name = soup.find('span', {'class': 'cmp-product-details-main__heading-title'}).get_text()
            description = soup.find('span', {'class': 'body'}).get_text()
            calories = soup.find('div', {'class': 'cmp-product-details-main__sub-heading'}).get_text()

            print(name)
            # Знаходимо кнопку і клікаємо
            button = driver.find_element(By.CLASS_NAME, 'cmp-accordion__button')
            button.click()

            # Додаткові дані
            all_nutritional_value = soup.find_all('li', {'class': 'cmp-nutrition-summary__heading-primary-item'})

            # Очищаємо текст: видаляємо зайві пробіли та заміняємо послідовні пробіли на один
            nutritional_value = [re.sub(r'\s+', ' ', i.get_text().strip()) for i in all_nutritional_value]

            fats = nutritional_value[1] if len(nutritional_value) > 1 else None
            carbs = nutritional_value[2] if len(nutritional_value) > 2 else None
            proteins = nutritional_value[3] if len(nutritional_value) > 3 else None

            all_supplements = soup.find_all('li', {'class': 'label-item'})
            supplements = [re.sub(r'\s+', ' ', s.get_text().strip()) for s in all_supplements]

            sugar = supplements[1] if len(supplements) > 1 else None
            salt = supplements[2] if len(supplements) > 2 else None

            # Зберігаємо дані в словник
            data = {
                'url': url,
                'name': name,
                'calories': calories,
                'description': description,
                'fats': fats,
                'carbs': carbs,
                'proteins': proteins,
                'sugar': sugar,
                'salt': salt
            }

            # Додаємо дані до загального списку
            all_data.append(data)

            # Очікування після кліку
            time.sleep(3)

        except Exception as e:
            print(f"Error processing {url}: {e}")

    # Записуємо всі зібрані дані в JSON файл
    with open('scraped_data.json', 'w') as f:
        json.dump(all_data, f, indent=4)

    # Закриваємо драйвер
    driver.quit()

scrape()
