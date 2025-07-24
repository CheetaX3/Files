#  --- Импорт модуля requests ---
import requests

# --- Отправка GET-запроса на сайт 'https://google.com' ---
response = requests.get('https://google.com')

# --- Проверка статус-кода ответа ---
if response.status_code == 200:
    print('Запрос выполнен успешно')
else:
    print('Произошла ошибка:', response.status_code)

# --- Вывод содержимого ответа ---
print(response.text)
