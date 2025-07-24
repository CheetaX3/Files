# 1
a = int(input('Enter the number 1:'))
b = int(input('Enter the number 2:'))
print (f'The numbers from {a} to {b} are:')
for i in range (a, b+1):
    print(i, end = ' ')

# 2
a = 2
b = 200
increment = 3
print (f'numbers from {a} to {b} in increments of {increment}:')
for i in range (a, b+1, increment):
    print(i, end = ' ')

# 3
n = int(input('Enter the number:'))
print (f'squares of numbers from 1 to {n} are:')
for i in range (1, n+1):
    print(i**2, end = ' ')

# 4
a = 100
b = 500
sum = 0
print (f'sum of numbers from {a} to {b} is:')
for i in range (a, b+1):
    sum += i
print(sum)

# 5
a = int(input('Enter the number 1:'))
b = int(input('Enter the number 2:'))
i_num = 0
i_sum = 0
for i in range (a, b+1):
    i_sum += i
    i_num += 1
print (f'the number of integers is {i_num}, sum is {i_sum}')

# 6
a = int(input('Enter the number:'))
print (f'Positive integers up to {a}:')
for i in range (1, a):
    print(i, end = ' ')

# 7 Исправил, тут совсем было неверно
print (f'The first number of the row that is greater than {n}:')
num = a = 1
while num <= n:
    num = (a + 1)**2
    a += 1
print(num)

# 8 
number = int(input('Enter the number:'))
while number > 9:
     number = number//10
print (f'The first digit of the number is' + str(number))

# 9
number = int(input('Enter a number: '))
num_sum = 0
while number > 0:
    num_sum += number % 10
    number = number//10
print(num_sum)

# 10  
seq = [1, 2, 3, 0]
summa = 0
for i in seq:
    if i != 0:
        summa += int(i)
    else:
        break
print('The sum of the sequence numbers is', summa)

# 11
seq = [5, 5, -7, 5]
all_numbers_equal = True

if not seq  or seq[0] < 0:
    all_numbers_equal = False
else:
    for num in seq:
        if num < 0:
            break
        if seq[0] != num:
            all_numbers_equal = False
            break

print(all_numbers_equal)

# 12
print('''Enter a sequence of positive number less than 30 000. 
After entering each number, press enter. 
The last number of the sequence must be zero.''')

# создание списка, удовлетворяющего условиям: количество элементов <= 1000, значения элементов <= 30000
my_list = []
my_list_len = 0

while my_list_len <= 1000:
    i = int(input())
    if i == 0:
        break
    if 0 < i <= 30000:
        my_list.append(i)
        my_list_len += 1
    else:
        if i > 30000:
            print('The number is more than 30000')
        else:
            print('The number is negative')

# поиск количества элементов, удовлетворяющих условиям: кратное 2 и 7 
num = 0
for i in range(len(my_list)):
    if my_list[i] % 2 == 0 and my_list[i] % 7 == 0:
        num += 1
print(f'The number of numbers divisible by 2 and 7 is {num}') if num != 0 else print('There are no numbers divisible by 2 and 7 in the sequence')

# 13 Как же все просто, когда знаешь "кое-что" про float('inf')
print('''Enter a sequence of positive number less than 30 000. 
After entering each number, press enter. 
The last number of the sequence must be zero.''')

# создание списка, удовлетворяющего условиям: количество элементов <= 1000, значения элементов <= 30000
my_list = []
my_list_len = 0

while my_list_len <= 1000:
    i = int(input())
    if i == 0:
        break
    if 0 < i <= 30000:
        my_list.append(i)
        my_list_len += 1
    else:
        if i > 30000:
            print('The number is more than 30 000')
        else:
            print('The number is negative')

min_val = float('inf')
for a in my_list:
    if a % 3 == 0 and a < min_val:
        min_val = a

print(f'The minimum number divisible by 3 is {min_val}' if min_val != float('inf') else 'There are no numbers divisible by 3 in the sequence')

# 14
print('''Enter a sequence of numbers. 
After entering each number, press enter. 
The last number of the sequence must be zero.''')

# создание списка, удовлетворяющего условиям: количество элементов <= 1000, значения элементов <= 30000
my_list = []
my_list_len = 0

while my_list_len <= 1000:
    i = int(input())
    if i == 0:
        break
    if 0 < i <= 30000:
        my_list.append(i)
        my_list_len += 1
    else:
        if i > 30000:
            print('The number is more than 30000')
        else:
            print('The number is negative')

num = 0
for i in my_list:
    if i % 3 ==0 or i % 7 == 0:
        num += 1
print(f'The number of numbers divisible by 3 or 7 is {num}') if num != 0 else print('There are no numbers divisible by 3 or 7 in the sequence')

# 15
n = int(input('Enter the number of observation days: '))
list_temp = []
num_pos = 0
for i in range(n):
    list_temp.append(int(input(f'Enter the temperature of day {i+1}: ')))
    if list_temp[i] > 0:
        num_pos += 1
print(f'The average temperature is {sum(list_temp)/n}')
if num_pos >=5:
    print('Yes')
else:
    print('No')

# 16
n = int(input('Enter how many natural numbers less than 1000 you will input: '))
min_val = float('inf')
count = 1

while count <= n:
    num = int(input(f'Enter the natural number {count}: '))
    if 0 < num <= 30000:
        count += 1
        if num % 2 == 0 and num < min_val:
            min_val = num
    else:
        if num > 30000:
            print('The number is more than 30 000')
        else:
            print('The number is negative')

print(f'The minimum even number is {min_val}' if min_val != float('inf') else 'There are no even numbers in the sequence')

# 17
# создание списка скоростей авто с условиями: количество элементов <= 30, скорость > 0
print('''Enter the speed of the cars. 
The number of cars should not exceed 30. 
To end the input, enter zero.''')

count = 1
exceed_80 = False
min_speed = float('inf')

while count <= 30:
    speed = int(input(f'Enter the speed of the car {count}: '))
    if speed == 0: # условие для выхода из цикла
        break
    if not exceed_80 and speed > 80:
        exceed_80 = True
    if 300 >= speed > 0:
        if speed < min_speed:
            min_speed = speed
        count += 1
    else:
        print('The speed cannot be negative or greater than 300.')   

print(min_speed, end=' ')
print('YES') if exceed_80 else print('NO')
