# 1 Проверить, что каждое слово в строке начинается с большой буквы

a = 'Hello hello'
print(a.istitle())


# 2 Проверить строку на вхождение в нее другой строки
a = 'Hello, Alexander'
b = 'Alexander'
print(b in a)


# 3 Найти индекс первого вхождения подстроки в строку

a = 'Hello, Alexander'
print(a.index('ll'))


# 4 Подсчитать количество символов в строке

a = 'Hello, Alexander'
print(len(a))


# 5 Подсчитать сколько раз определенный символ встречается в строке

a = 'Hello, Alexander'
print(a.count('l'))


# 6 Сделать первый символ строки заглавной буквой

a = 'hello, Alexander'
print(a.capitalize())

# или второй вариант, если хочу оставить остальные буквы в прежнем регистре

a = 'hello, Alexander'
a = a[0].upper() + a[1:]
print(a)


# 7 f-строки и как пользоваться 

name = 'Alexander'
type = 'backend'
text = f'Hey {name}! Come join the best Python course for {type} developers - you\'ll love it!'
print(text)


# 8 Найти подстроку в заданной части строки

a = 'Hello, Alexander'
print(a.find('lex', 5, 11))


# 9 Узнать о том, что в строке есть только цифры

a = '1234A5'
print(a.isdigit())


# 10 Разделить строку по заданному символу

a = 'Hello, Alexander'
print(a.split(','))


# 11 Проверить строку на то, что она составлена только из строчных букв

a = 'helloalexander'
print(a.islower())
print(a.isalpha())


# 12 Проверить то, что строка начинается со строчной буквы

a = 'Hello, Alexander'
print(a[0].islower())


# 13 "Перевернуть» строку

a = 'Hello'
print(a[::-1])


# 14 Объединить список строк в одну строку, элементы которой разделены дефисами

a = ['Hello', 'Alexander', 'Python']
print('-'.join(a))


# 15 Проверить строку на то, что она составлена только из прописных букв

a = 'HELLOALEXANDER'
print(a.isupper())
print(a.isalpha())


# 16 Узнать о том, что строка содержит только алфавитные символы

a = 'HelloAlexander'
print(a.isalpha())


# 17 В заданной строке заменить на что-либо все вхождения некоей подстроки

a = 'Hello, Alexander'
print(a.replace('l', 'L'))


# 18 Проверить строку на то, что в ней содержатся только алфавитно-цифровые символы

a = 'Hello555Alexander'
print(a.isalnum())


# 19 Проверить то, что строка начинается с заданной последовательности символов, или заканчивается заданной последовательностью символов

a = 'Hello, Alexander'
print(a.startswith('Hello'))
print(a.endswith('Alexander'))


# 20 Узнать о том, что строка включает в себя только пробелы

a = 'Hello, Alexander'
print(a.isspace())


# 21 Привести к верхнему регистру первый символ каждого слова в строке

a = 'hello, alexander'
print(a.title())
