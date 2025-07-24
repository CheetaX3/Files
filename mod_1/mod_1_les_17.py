# 1 Вывести True если число положительное, и False если нет
a = int(input('Enter the number: '))
if a > 0:
    print('Positive')
elif a < 0:
    print('Negative')
else:
    print('Zero')

# 2 Дано число х. Проверьте нечетное ли оно? Если нечетное вывести True, если нет False. 
# (Подсказка: у четного числа остаток при делении на 2 будет равен 0)
x = int(input('Enter the number: '))
if x % 2 != 0:
    print('нечетное')
else:
    print('четное')

# 3 Напишите программу, которая проверяет последнюю цифру числа. 
# Если последняя цифра числа 3, то вывести True иначе вывести False.
x = int(input('Enter the number: '))
print(x % 10 == 3)

# 4 Напишите программу, которая выводит True, если число х принадлежит промежутку [0,15], 
# и False если не принадлежит
x = int(input('Enter the number: '))
print(x in range(16))

# 5 Напишите программу, которая выводит True если число Х кратно 3 и заканчивается на 5. 
# Число х вводится с клавиатуры
x = int(input('Enter the number: '))
print(x % 3 == 0 and x % 10 == 5)

# 6 Даны два числа определить какое из них больше. 
# Вывести ответ(Первое больше / Второе больше/Равны)
a = int(input('Enter the number A: '))
b = int(input('Enter the number B: '))
if a > b:
    print('A is greater than B')
elif a < b:
    print('B is greater than A')
else:
    print('A is equal to B')

# 7 Найти количество четных чисел среди заданных трех целых чисел. 
# В ответе вывести количество четных чисел.
num_1 = int(input('Enter the number 1: '))
num_2 = int(input('Enter the number 2: '))
num_3 = int(input('Enter the number 3: '))
nums_sum = 0
if num_1 % 2 == 0:
    nums_sum += 1
if num_2 % 2 == 0:
    nums_sum += 1
if num_3 % 2 == 0:
    nums_sum += 1
print(f'The number of even numbers = {nums_sum}')

# 8 Известен номер месяца (от 1 до 12). Вывести название месяца. 
# (январь/февраль/март/апрель/май/июнь/июль/август/сентябрь/октябрь/ноябрь/декабрь) 
months = {
    1: 'January', 2: 'February', 3: 'March', 
    4: 'April', 5: 'May', 6: 'June', 
    7: 'July', 8: 'August', 9: 'September', 
    10: 'October', 11: 'November', 12: 'December'
}
month = int(input('Enter the number of the month: '))
print(months.get(month, 'Invalid month'))

# 9 Дано трехзначное число. Кратна ли числу 3 сумма его цифр. (Ответ: Да/Нет)
number = int(input('Enter a three-digit number: '))
num_sum = 0
while number > 0:
    num_sum += number % 10
    number = number//10
print(num_sum % 3 == 0)

# 10 Год является високосным, если:
# год кратен 400 (например 1600, 1200, 2000)
# год кратен 4, но некратен 100 (например 2004, 1996 - високосные, 1900 - невисокосный) остальные года невисокосные. 
# Определите является ли введенный с клавиатуры год високосным. 
# (Ответ: високосный/невисокосный)
year = int(input('Enter the year: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('True')
else:
    print('False')

# 11 Дано положительное число х (х<1000). Определить, какое оно: однозначное, двузначное, трехзначное. 
# (Ответы: однозначное/двузначное/трехзначное)
number = int(input('Enter a number less than 1000: '))
digits = 0
while number > 1:
    number /= 10
    digits += 1

print(str(digits) + '-digit number')

# 12 В первой строке даны два числа a и b.
# Во второй строке дано одно число означающее арифметическую операцию: 
# "1"- сложение, "2"-вычитание, "3"-умножение, "4"-деление. 
# Определите результат операции над числами a и b. (второе число не равно нулю)
numbers = list(map(int, input('Enter two numbers: ').split()))
operator = input('Enter a number of the operation (1 - addition, 2 - subtraction, 3 - multiplication, 4 - division): ')
if operator == '1':
    print(numbers[0] + numbers[1])
elif operator == '2':
    print(numbers[0] - numbers[1])
elif operator == '3':
    print(numbers[0] * numbers[1])
elif operator == '4':
    print(numbers[0] / numbers[1])