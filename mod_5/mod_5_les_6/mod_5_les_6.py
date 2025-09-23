import datetime as dt
import locale
import platform


if platform.system() == "Windows":
    # Для Windows
    locale.setlocale(locale.LC_TIME, "Russian_Russia.1251")
else:
    # Для Linux / macOS
    locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")

now_date = dt.datetime.now()
print("День по счету:", now_date.day)

today_date = dt.datetime.today()
print("День недели:", today_date.strftime("%A"))

if now_date.year % 4 == 0 and (now_date.year % 100 != 0 or now_date.year % 400 == 0):
    print('Текущий год високосный')
else:
    print('Текущий год не високосный')

new_date = input('Введите дату в формате ГГГГ-ММ-ДД: ')
new_date = dt.datetime.strptime(new_date, "%Y-%m-%d")
difference = new_date - now_date

days = difference.days
hours, remainder = divmod(difference.seconds, 3600)
minutes, _ = divmod(remainder, 60)

print(f"Разница: {days} дней, {hours} часов, {minutes} минут")