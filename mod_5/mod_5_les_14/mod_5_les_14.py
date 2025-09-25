fruits = ["apple", "kiwi", "banana", "fig"]
filtered_fruits = filter(lambda x: len(x) > 4, fruits)
print(list(filtered_fruits))

students = [{"name": "John", "grade": 90}, {"name": "Jane", "grade": 85}, {"name": "Dave", "grade": 92}]
best_student = max(students, key=lambda x: x["grade"])
print(best_student["name"])

pairs = [(1, 5), (3, 2), (2, 8), (4, 3)]
sorted_pairs = sorted(pairs, key=lambda x: x[0] + x[1])
print(sorted_pairs)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        
        return f"Person(name={self.name}, age={self.age})"


people = [
    Person("John", 25),
    Person("Jane", 5),
    Person("Dave", 15)
]

sorted_people = sorted(people, key=lambda x: x.age)
print(sorted_people)
