# задание 1
from pathlib import Path
import csv

BASE_DIR = Path(__file__).parent
txt_path = BASE_DIR / 'prices.txt'
csv_path = BASE_DIR / 'prices.csv'

with open(txt_path, 'r', encoding='utf-8') as f:
    data = [line.strip().split('\t') for line in f]

with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerows(data)


# задание 2
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)

    total_sum = 0
    for row in reader:
        total_sum += int(row[1]) * int(row[2])

print(total_sum)