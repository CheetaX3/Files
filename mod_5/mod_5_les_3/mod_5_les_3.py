from pathlib import Path
import json


def csv_to_dicts(csv_path, delimiter=";"):
    """Преобразует CSV в список словарей, где первая строка — заголовки."""
    with open(csv_path, "r", encoding="utf-8") as f:
        lines = [line.strip().split(delimiter) for line in f]

    headers = lines[0]
    rows = lines[1:]

    result = []
    for row in rows:
        pairs = zip(headers, row)
        d = dict(pairs)
        result.append(d)

    return result


BASE_DIR = Path(__file__).parent
csv_path = BASE_DIR / "prices.csv"

data = csv_to_dicts(csv_path)
print(json.dumps(data, ensure_ascii=False, indent=4))