# Задание 2
from pathlib import Path
import csv
import locale
import platform
import datetime

if platform.system() == "Windows":
    # Для Windows
    locale.setlocale(locale.LC_TIME, "Russian_Russia.1251")
else:
    # Для Linux / macOS
    locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")

BASE_DIR = Path(__file__).parent
csv_path = BASE_DIR / "sales.csv"

with open(csv_path, "r", encoding="utf-8-sig", newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    rows = list(reader)

total_sales = 0
for row in rows[1:]:
    total_sales += int(row[2])

max_sale_amount = 0
max_sale_product = None
for row in rows[1:]:
    sale_amount = int(row[2])
    if sale_amount > max_sale_amount:
        max_sale_amount = sale_amount
        max_sale_product = row[1]

month_sales = {}
for row in rows[1:]:
    date = datetime.datetime.strptime(row[0], "%Y-%m-%d")
    month = date.strftime("%B")
    month_sales[month] = month_sales.get(month, 0) + int(row[2])

print(f"Общая сумма продаж: {total_sales} рублей")
print(f"Наиболее продаваемый товар: {max_sale_product}")
print("Продажи по месяцам:")
for month, sales in month_sales.items():
    print(f"{month}: {sales}")