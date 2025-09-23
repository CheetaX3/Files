import itertools

#  Задание 1
list1 = [1, 2, 3, 4]
l1 = itertools.combinations(list1, 2)
print(list(l1))

# Задание 2
word1 = 'Python'
for i in itertools.permutations(word1):
    print(i)

# Задание 3
list1 = ['a', 'b']
list2 = [1, 2, 3]
list3 = ['x', 'y']
list4 = list1 + list2 + list3

count = 1
for item in itertools.cycle(list4):
    if count > len(list4)*5:
        break
    print(item, end=' ')
    count += 1

# Задание 4
def fibonacci():
    a, b = 0, 1
    for _ in itertools.count():  # бесконечный цикл
        yield a
        a, b = b, a + b


print(list(itertools.islice(fibonacci(), 10)))

# Задание 5
list1 = ['red', 'blue']
list2 = ['shirt', 'shoes']

for item in itertools.product(list1, list2):
    print(item)
