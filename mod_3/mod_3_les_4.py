class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a positive integer.")
        self._age = value

person = Person("John", -25)
print(person.age)  # Вывод: 25

person.age = 30
print(person.age)  # Вывод: 30

person.age = -5  # Вызов исключения ValueError: Age must be a positive integer.