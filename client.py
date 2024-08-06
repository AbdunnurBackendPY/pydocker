import requests
import json

# Загрузка данных из JSON файла
with open('data.json', 'r') as f:
    data = json.load(f)

# URL вашего Flask-приложения
url = 'http://127.0.0.1:5000/calculate'

try:
    # Отправка POST-запроса с данными
    response = requests.post(url, json=data)
    response.raise_for_status()  # Проверка наличия HTTP ошибок
    # Вывод ответа
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")




