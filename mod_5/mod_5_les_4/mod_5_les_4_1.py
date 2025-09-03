# Задание 1
from pathlib import Path
import json

BASE_DIR = Path(__file__).parent
json_path = BASE_DIR / "students.json"

with open(json_path, "r", encoding="utf-8-sig") as json_file:
    data = json.load(json_file)

students_num = 0
max_age = 0
oldest_student = None

for student in data:
    students_num += 1
    if student["возраст"] > max_age:
        max_age = student["возраст"]
        oldest_student = student

print("Количество студентов:", students_num)

if oldest_student:
    print(
        f"Самый старший студент: {oldest_student['имя']}, "
        f"возраст: {oldest_student['возраст']} года/лет, "
        f"город: {oldest_student['город']}"
    )

subject = input(
    "Введите предмет для подсчета количества изучающих его студентов: "
)
count = 0

for student in data:
    subjects_lower = [s.lower().replace(" ", "") for s in student["предметы"]]
    if subject.lower().replace(" ", "") in subjects_lower:
        count += 1

print(f"Количество студентов, изучающих {subject}: {count}")