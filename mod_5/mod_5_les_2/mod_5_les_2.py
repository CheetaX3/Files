# задание 1
import csv

txt_path = r'mod_5\mod_5_les_2\prices.txt'
csv_path = r'mod_5\mod_5_les_2\prices.csv'

with open(txt_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

data = [line.strip().split('\t') for line in lines]

with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerows(data)


# задание 2
csv_path = r'mod_5\mod_5_les_2\prices.csv'

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)

    total_sum = 0
    for row in reader:
        total_sum += int(row[1]) * int(row[2])

print(total_sum)