# Задание 1 Функция определяет среднее значение чисел
def calculate_average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

print(calculate_average(1, 2, 3))

# Задание 2 Функция определяет четное или нечетное число
def is_even(number1):
    return number1 % 2 == 0

print(is_even(4))

# Задание 3 Функция определяет кол-во гласных в строке
def count_vowels(text):
        text_low = text.lower()
        vowels = ['a', 'o', 'u', 'e', 'i', 'y']
        sum_vowels = 0
        for i in text_low:
            if i in vowels:
                sum_vowels += 1
        return sum_vowels

print(count_vowels('Alexander'))

# Задание 4 Функция определяет наибольшее число из списка
def find_max(*args):
    min_number = float('-inf')
    for i in args:
        if i > min_number:
            min_number = i
    return(min_number)

print(find_max(5, 2, 3))

# Задание 5 Функция переворачивает строку наоборот
def reverse_string(text):
    return text[::-1]

print(reverse_string('Alexander'))

# Задание 6 Функция определяет является ли текст палиндромом
def is_palindrome(text):
    return text.lower() == text.lower()[::-1]
    
print(is_palindrome('Amma'))

# Задание 7 Функция вычисляет факториал числа
def calculate_factorial(number1):
    fac = 1
    for i in range(1, number1+1):
        fac *= i
    return fac

print(calculate_factorial(5))

# Задание 8 Функция определяет является ли число простым
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(is_prime(11))

# Задание 9 Функция возвращает последовательность Фибоначчи
def generate_fibonacci(n):
    a = 0
    b = 1
    my_list = []
    for i in range(n):
        my_list.append(a)
        a, b = b, a + b
    return my_list

print(generate_fibonacci(4))

# Задание 10 Возвращает список слов с заглавной буквы
def capitalize_names(*args):
    my_list = []
    for i in args:
        my_list.append(i.capitalize())
    return my_list


print(capitalize_names('alexander', 'fedor', 'michael'))