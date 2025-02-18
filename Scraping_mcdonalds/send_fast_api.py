import json
from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

# Створюємо екземпляр FastAPI
app = FastAPI()

# Модель продукту для валідації даних
class Product(BaseModel):
    name: str
    description: str
    calories: str
    fats: Optional[str] = None
    carbs: Optional[str] = None
    proteins: Optional[str] = None
    sugar: Optional[str] = None
    salt: Optional[str] = None

# Функція для зчитування даних з файлу JSON
def load_products():
    with open('scraped_data.json', 'r') as file:
        return json.load(file)

# Отримання всіх продуктів

@app.get("/all_products/", response_model=List[Product])
async def get_all_products():
    # Зчитуємо продукти з файлу
    products = load_products()
    return products


# Отримання продукту за його ім'ям
@app.get("/products/{product_name}", response_model=Product)
async def get_product_by_name(product_name: str):
    # Зчитуємо продукти з файлу
    products = load_products()

    # Шукаємо продукт за іменем
    for product in products:
        if product["name"].lower() == product_name.lower():
            return product

    # Якщо продукт не знайдений, кидаємо помилку 404
    raise HTTPException(status_code=404, detail="Product not found")


# Отримання інформації про конкретне поле продукту
@app.get("/products/{product_name}/{product_field}")
async def get_product_field(product_name: str, product_field: str):
    # Зчитуємо продукти з файлу
    products = load_products()

    # Шукаємо продукт за іменем
    for product in products:
        if product["name"].lower() == product_name.lower():
            # Перевірка, чи існує таке поле в продукті
            if product_field in product:
                return {product_field: product[product_field]}
            else:
                raise HTTPException(status_code=404, detail=f"Field '{product_field}' not found for this product")

    # Якщо продукт не знайдений
    raise HTTPException(status_code=404, detail="Product not found")