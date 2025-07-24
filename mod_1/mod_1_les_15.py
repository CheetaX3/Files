# 1

primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
print(primes[:6])

# 2

data = 'Python for advanced users'
print(tuple(data))

# 3

numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
numbers = list(numbers)
print(max(numbers) + min(numbers))

# 4

my_string1 = '133659854125365'
my_string2 = '1336598541253657'
print(set(my_string1) == set(my_string2))

# 5 для определения общего количества уникальных слов в тексте необходимо удалить все знаки препинания
# придется воспользоваться материалом, который на данном этапе еще не включен в курс

import string

my_str = 'Snowflakes, snowflakes falling down. Snowflakes, covering up the ground. Making a blanket, soft and white. Making a blanket in the night.'
clean_str = my_str.translate(str.maketrans('', '', string.punctuation))
lower_str = clean_str.lower()
set_str = set(lower_str.split())
print(len(set_str))

# 6

import string

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning)
when I was three, and, save for a pocket of warmth in the darkest past, nothing of her
subsists within the hollows and dells of memory, over which, if you can still stand my style
(I am writing under observation), the sun of my infancy had set: surely, you all know those redolent
remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and
traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
clean_str = sentence.translate(str.maketrans('', '', string.punctuation))
lower_str = clean_str.lower()
set_str = set(lower_str.split())
print(sorted(list(set_str)))

# 7

a = input('Enter a natural number: ')
a = a.replace('0', 'zero ')
a = a.replace('1', 'one ')
a = a.replace('2', 'two ')
a = a.replace('3', 'three ')
a = a.replace('4', 'four ')
a = a.replace('5', 'five ')
a = a.replace('6', 'six ')
a = a.replace('7', 'seven ')
a = a.replace('8', 'eight ')
a = a.replace('9', 'nine ')
print(a)