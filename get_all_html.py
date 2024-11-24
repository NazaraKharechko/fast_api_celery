import time
import requests

# Вказуємо URL сторінки, яку хочемо запросити
urls = []

for href in range(2008, 2025):
    urls.append(f'https://web.archive.org/web/{href}/http://www.businessconsultingabc.com/')
print(len(urls))

# for url in urls:
#     try:
#         # Виконуємо GET-запит
#         response = requests.get(url)
#         status_code = response.status_code
#
#         # Отримуємо HTML-розмітку сторінки
#         html_content = response.text
#
#         # Виводимо статус-код
#         print(f"Status Code: {status_code}")
#
#         # Зберігаємо HTML-розмітку у файл
#         with open(f'webpage_{url[28:32]}.html', 'w', encoding='utf-8') as file:
#             file.write(html_content)
#
#         print(f"HTML content has been saved to 'webpage_{url[28:32]}.html'")
#
#         # Збільшуємо затримку між запитами
#         time.sleep(2)
#     except requests.exceptions.RequestException as e:
#         # Обробка винятків
#         print(f"An error occurred: {e}")
#         # Затримка перед повторною спробою
#         time.sleep(2)
