# 1

numbers = [int(x) for x in input().split()]    # можно другой вариант numbers = list(map(int, input().split()))
print (sum(numbers))

# 2

my_list = input().split()
for i in range(0, len(my_list), 2):
    print(my_list[i], end=' ')

#  3

numbers = [int(x) for x in input().split()]
print(round(sum(numbers) / len(numbers), 3))

# 4

chance = input()
heads = chance.count('О')
tails = chance.count('Р')
heads_proc = round(heads / (heads + tails) * 100)
tails_proc = 100 - heads_proc
print(f'Процент выпадений Орла: {heads_proc}\nПроцент выпадений Решки: {tails_proc}')
