# проверка окончания числа на 3
x = int(input('Enter the number: '))
ends_with_three = x % 10 == 3

if not ends_with_three:
    print('Does not end with 3')

# проверка окончания числа на 3 (другой вариант)
x = int(input('Enter the number: '))
ends_with_three = False

if x % 10 == 3:
    ends_with_three = True

print(ends_with_three)

# способ проверить кучу условий без if-else (guard clause)
def log_in(authenticated: bool, authorized: bool):
    success = True
    msg = 'success!'

    if not authenticated:
        success = False
        msg = 'not authenticated'

    if not authorized:
        success = False
        msg = 'not authorized'
   
    return success, msg

# объявление функций
def greet(name: str = "Guest"):  # Параметр с значением по умолчанию
    print(f"Hello, {name}")

# 
print(('нет','да')[len(set(input().split())) == 1])

