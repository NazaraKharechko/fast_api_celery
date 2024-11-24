import requests
from requests.exceptions import RequestException
import json
import time

# Зчитування посилань із файлу
with open('links.json', 'r') as f:
    res = json.load(f)


def make_request(url, retries=3, timeout=10):
    for i in range(retries):
        try:
            response = requests.get(url, timeout=timeout)
            return response
        except RequestException as e:
            print(f"Request failed: {e}. Retrying ({i+1}/{retries})...")
            time.sleep(2)  # Затримка перед повторною спробою
    return None


# Отримаємо html з посилань
for html in res:
    full_url = f'{html}'
    response = make_request(full_url)
    if response:
        print(response.status_code)
        if response.status_code == 200:
            print(full_url)
            print(response.text)
            break
            # Тут можна додати код для обробки отриманого контенту
    else:
        print(f"Failed to retrieve {full_url} after multiple attempts.")
