# Задание 3
from pathlib import Path
import json
import csv

BASE_DIR = Path(__file__).parent
json_path = BASE_DIR / 'employees.json'
csv_path = BASE_DIR / 'performance.csv'

with open(json_path, "r", encoding="utf-8-sig",newline="") as json_file:
    employees = json.load(json_file)

with open(csv_path, "r", encoding="utf-8-sig", newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    rows = list(reader)

for employee in employees:
    for row in rows[1:]:
        if int(row[0]) == employee["id"]:
            employee["производительность"] = int(row[1])
            break

total_performance = 0
for employee in employees:
    total_performance += employee["производительность"]

average_performance = total_performance / len(employees)

best_employee = None
best_performance = 0
for employee in employees:
    if employee["производительность"] > best_performance:
        best_performance = employee["производительность"]
        best_employee = employee

print(f"Среднее значение производительности: {average_performance}")
print(
    f"Лучший сотрудник: {best_employee['имя']}, "
    f"производительность: {best_performance}"
)