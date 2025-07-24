# Практикум 1

# Задание 1
name = input('Enter your name: ')
print('Hello, ' + name)

# Задание 2
str1 = input('Enter the first string: ')
str2 = input('Enter the second string: ')
str3 = input('Enter the third string: ')
print(str3, str2, str1, sep='\n')

# Задание 3
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print((a + b)/2)

# Задание 4
temp_F = float(input('Enter the temperature in Fahrenheit: '))
temp_C = round((temp_F - 32) * 5 / 9, 2)
print(temp_C)

# Задание 5
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))
a1 = max(n1, n2, n3)
a2 = min(n1, n2, n3)   
a3 = n1 + n2 + n3 - a1 - a2
print(a1, a3, a2)

# Задание 6
symbols = input('Enter a string longer than 4 characters: ')
print(symbols[0], symbols[3], sep = ' ')
print(symbols[-1], symbols[-2], sep = ' ')