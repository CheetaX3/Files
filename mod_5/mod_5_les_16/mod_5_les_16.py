# Задание 0. Работа с json
# Считываем данные из файла student_list.json
# и преобразовываем в словарь students

import json
import csv
from pathlib import Path
import itertools


BASE_DIR = Path(__file__).parent
json_path = BASE_DIR / "student_list.json"
csv_path = BASE_DIR / 'student_list.csv'

with open(json_path, "r", encoding="utf-8") as f:
    students = json.load(f)

# Задание 1: Средний балл по всем предметам
# Функция get_average_score(), которая вычисляет
# средний балл по всем предметам для каждого студента
# в словаре students и выводит результат в формате:
# Средний балл для студента John: 85.0


def get_average_score():
    averages = {}
    for name, info in students.items():
        grades = info.get("grades", {})
        if grades:
            avg = sum(grades.values()) / len(grades)
            averages[name] = round(avg, 2)
        else:
            averages[name] = None
    return averages


averages = get_average_score()

for name, avg in averages.items():
    if avg is not None:
        students[name]["avg"] = avg
        print(f"Средний балл для студента {name}: {avg}")
    else:
        students[name]["avg"] = None
        print(f"У студента {name}: нет оценок")

# Задание 2: Наилучший и худший студент
# Функции get_best_student() и get_worst_student(),
# которые находят студента с наилучшим и худшим средним баллом соответственно.
# Выводят их имена и средние баллы в следующем формате:
# Наилучший студент: Sophia (Средний балл: 90.67)
# Худший студент: Robert (Средний балл: 83.67)


def get_worst_student():
    valid_students = {name: info["avg"] for name, info in students.items() if info["avg"] is not None}

    if not valid_students:
        return None, None

    worst_student = min(valid_students, key=valid_students.get)
    return worst_student, valid_students[worst_student]


def get_best_student():
    valid_students = {name: info["avg"] for name, info in students.items() if info["avg"] is not None}

    if not valid_students:
        return None, None

    best_student = max(valid_students, key=valid_students.get)
    return best_student, valid_students[best_student]


worst_student, worst_student_average = get_worst_student()
best_student, best_student_average = get_best_student()

print(f"Худший студент: {worst_student} (Средний балл: {worst_student_average})")
print(f"Наилучший студент: {best_student} (Средний балл: {best_student_average})")

# Задание 3: Поиск по имени
# Функция find_student(name), которая принимает имя студента
# в качестве аргумента и выводит информацию о нем, если такой студент
# есть в словаре students. В противном случае, выводит
# сообщение "Студент с таким именем не найден".


def find_student(name):
    if name in students:
        student_info = students[name]
        print(f"Имя: {name}")
        print(f"Возраст: {student_info['age']}")
        print(f"Предметы: {student_info['subjects']}")
        print(f"Оценки: {student_info['grades']}")
    else:
        print("Студент с таким именем не найден")

find_student("Emma1")


# Задание 4: Сортировка студентов
# Сортировка студентов по их среднему баллу в порядке убывания.
# Вывод имен студентов и их средних баллов в следующем формате:
# Сортировка студентов по среднему баллу:
# Sophia: 90.67
# Michael: 85.0
# John: 85.0
# Robert: 83.67
# Alice: 83.33


def sort_students():
    def average(grades: dict) -> float:
        return sum(grades.values()) / len(grades) if grades else 0

    students_with_avg = [
        (name, average(info.get("grades", {})))
        for name, info in students.items()
    ]

    sorted_students = sorted(students_with_avg, key=lambda x: x[1], reverse=True)
    return sorted_students


for name, average in sort_students():
    print(f"{name}: {average}")


# Задание 5. Преобразование словаря в список словарей данного формата

students_list = list(itertools.starmap(lambda name, data: {"name": name, **data}, students.items()))
print(students_list)


# Задание 6. Формирование csv

with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for name, info in students.items():
        writer.writerow({
            "name": name,
            "age": info["age"],
            "grade": round(sum(info["grades"].values()) / len(info["grades"]), 2)
        })
