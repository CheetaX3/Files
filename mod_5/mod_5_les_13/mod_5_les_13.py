from functools import reduce


def pow_3(x):
    return x ** 3


numbers1 = [1, 2, 3]
new_numbers1 = map(pow_3, numbers1)
print(list(new_numbers1))


def multiple_of_5(x):
    return x % 5 == 0


numbers2 = [5, 2, 3, 10]
new_numbers2 = filter(multiple_of_5, numbers2)
print(list(new_numbers2))


def is_not_even(x):
    return x % 2 != 0


def multiply(x, y):
    return x * y


numbers3 = [5, 2, 3, 10]
filtered_numbers3 = filter(is_not_even, numbers3)
new_numbers3 = reduce(multiply, filtered_numbers3)
print(new_numbers3)
