#  Задание 1

numbers = list(input('Enter two numbers separated by a space: ').split())
try:
    sum_numbers = int(numbers[0]) + int(numbers[1])
    print(sum_numbers)
except ValueError:
    print('You entered a text instead of a number')
    concatenated_numbers = numbers[0] + numbers[1]
    print(concatenated_numbers)


#  Задание 2

def check_password(password):
    result = "Password requirements are met"

    try:
        if not password:
            raise ValueError("You entered an empty password!")
        if password.isdigit():
            raise ValueError("Password contains only digits")
    except ValueError as e:
        result = f'Ошибка: {e}'

    return result
