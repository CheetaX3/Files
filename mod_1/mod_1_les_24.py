# Задание 1
from random import choices
import string

symbols = list(string.ascii_letters + string.digits)
password_length = int(input('Enter the password length: '))
password = ''.join(choices(symbols, k=password_length))
print(password)


# Задание 2
from datetime import datetime

input_birth_date = input('Enter the date of birth in the format dd.mm.yyyy: ')
birth_date = datetime.strptime(input_birth_date, '%d.%m.%Y')

if datetime.now().month >= birth_date.month and datetime.now().day >= birth_date.day:
    delta = (datetime.now().year - birth_date.year) 
else:
    delta = (datetime.now().year - birth_date.year) - 1
print(delta)


# Задание 3
import string
import collections

input_text = input('Enter a text: ')
cleaned_text = input_text.lower().translate(str.maketrans("", "", string.punctuation))
print(collections.Counter(cleaned_text.split()))
print(cleaned_text.split())