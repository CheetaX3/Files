from dataclasses import dataclass
from operator import attrgetter

@dataclass
class Student:
    name: str # имя студента
    age: int # возраст студента
    major: str # специальность
    gpa: float # средний балл студента

    def display_info(self):
        print(f'Name: {self.name}, Age: {self.age}, Major: {self.major}, GPA: {self.gpa}')

    def calculate_grade(self):
        if self.gpa >= 4.5:
            return 'Отлично'
        elif 3.5 <= self.gpa < 4.5:
            return 'Хорошо'
        elif 2.5 <= self.gpa < 3.5:
            return 'Удовлетворительно'
        else:
            return 'Неудовлетворительно'

def sort_students_by_gpa(student_list):
    return sorted(student_list, key=attrgetter('gpa'), reverse=True)

# Создание списка студентов
students = [
    Student("Alice", 20, "Computer Science", 3.8),
    Student("Bob", 22, "Engineering", 3.2),
    Student("Charlie", 21, "Mathematics", 4.5),
    Student("David", 23, "Physics", 2.7),
    Student("Eve", 19, "Biology", 3.9),
]

# Сортировка студентов по среднему баллу
students = sort_students_by_gpa(students)

# Отображение информации о студентах
for student in students:
    student.display_info()

# Сравнение студентов
print("Are Alice and Bob the same student?", students[0] == students[1])
print("Are Alice and Eve the same student?", students[0] == students[4])

# Расчет и вывод оценок
for student in students:
    print(f"{student.name} - Grade: {student.calculate_grade()}")