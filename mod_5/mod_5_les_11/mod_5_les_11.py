from itertools import product, combinations
from pathlib import Path

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♣', '♦', '♥', '♠']

# генерируем стандартную колоду
deck = [f"{rank}{suit}" for rank, suit in product(ranks, suits)]
print(f"В колоде {len(deck)} карт")

while True:
    try:
        number_of_cards = int(input('Введите количество карт для поиска комбинаций (1–52): '))
        if 1 <= number_of_cards <= len(deck):
            break
        else:
            print("Ошибка: нужно ввести число от 1 до 52.")
    except ValueError:
        print("Ошибка: введите целое число.")

# генератор комбинаций
comb_gen = combinations(deck, number_of_cards)

# выводим первые 10 комбинаций для примера
# print(f"\nПервые 10 комбинаций из {number_of_cards} карт:")
# for i, combo in enumerate(comb_gen, start=1):
#     print(combo)
#     if i >= 10:
#         break
# print("...")

# сохраняем все комбинации в файл
BASE_DIR = Path(__file__).parent
txt_path = BASE_DIR / 'combinations.txt'

with open(txt_path, 'w', encoding='utf-8') as f:
    for combo in comb_gen:
        f.write(" ".join(combo) + "\n")
