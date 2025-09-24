from functools import reduce


numbers1 = [1, 2, 3]
powed_numbers1 = map(lambda x: pow(x, 2), numbers1)
print(list(powed_numbers1))

numbers2 = [5, 2, 3, 10]
filtered_numbers2 = filter(lambda x: x % 5 == 0, numbers2)
print(list(filtered_numbers2))

numbers3 = [5, 2, 3, 10]
filtered_numbers3 = filter(lambda x: x % 2 != 0, numbers3)
powed_numbers3 = reduce(lambda x, y: x * y, filtered_numbers3)
print(powed_numbers3)
