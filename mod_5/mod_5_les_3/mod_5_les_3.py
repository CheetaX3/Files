import csv
import json

csv_path = r'mod_5\mod_5_les_3\prices.csv'
json_path = r'mod_5\mod_5_les_3\prices.json'

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    
    rows = list(reader)
    print(rows)

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=4)