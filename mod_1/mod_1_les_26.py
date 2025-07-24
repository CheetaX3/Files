# Задание 1

numbers = list(range(1, 11))
square_numbers = [x**2 for x in numbers]
print(square_numbers)

# # Задание 2

numbers = list(range(1, 21))
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# Задание 3

numbers = list(range(1, 11))
square_numbers_from_n = [x**2 for x in numbers if x > 5]
print(square_numbers_from_n)

# Задание 4

text = 'Hello, world!'
text_upper = [x.upper() for x in text]
print(text_upper)

# Задание 5

words = ['apple', 'banana', 'cherry', 'orange']
words_from_n = [x for x in words if len(x) > 5]
print(words_from_n)