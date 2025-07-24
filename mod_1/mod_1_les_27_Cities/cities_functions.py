import random


# 1 функция принимает на вход имя файла с городами 
# и затем возвращает список городов из файла
def load_cities(filepath: str) -> list[str]:
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.strip().lower() for line in f if line.strip()]

# 2 функция записывает ходы игроков в файл
def write_answer(text: str, filepath: str) -> None:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text.strip() + '\n')

def write_answer_append(text: str, filepath: str) -> None:
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(text.strip() + '\n')


# 3 получаем букву, на которую должны ввести свой город
def get_last_char(city: str) -> str:
    return city[-1] if city[-1] not in 'ьыъ' else city[-2]


# 4 функция отвечает за проверку того,
# правильный город назвал игрок или нет
def validate_user_city(user_city: str, cities: list[str], current_city: str) -> bool:
    return user_city in cities and user_city[0] == get_last_char(current_city)


# 5 функция пытается найти подходящий город 
# в списке городов для хода компьютера
def get_computer_city(last_char: str, cities: list[str]) -> None | str:
    filtered = [city for city in cities if city.startswith(last_char)]
    if not filtered:
        print('Компьютер не может подобрать подходящий город.')
        return None
    return random.choice(filtered)

# 6 функция реализует основную логику игры
def game(CITIES_FILEPATH, ANSWERS_FILEPATH, MAX_ERRORS):

    print('''Добро пожаловать в игру "Угадай город"!
    Правила игры:
    - вы должны назвать город, который заканчивается на последнюю букву города, который назвал компьютер.
    Если последня буква города оканчивается на буквы "ь", "ъ" или "ы",
    то вы должны назвать город, который заканчивается на предпоследнюю букву.
    Если вы назвали город, соответствующий условиям, то компьютер называет следующий город.
    Повторно называть города нельзя.
    Вы выигрываете, если компьютер не сможет подобрать подходящий город хотя бы 1 раз.
    Выигрывает компьютер, если вы не назовете город 5 раз.
    '''
    )

    cities_list = load_cities(CITIES_FILEPATH)

    # --- Выбор первого города компьютером ---
    current_city = random.choice(cities_list)
    write_answer(f'Начальный город: {current_city}', ANSWERS_FILEPATH)
    cities_list.remove(current_city)
    error_counter = 0
    print(f'Компьютер назвал город: {current_city}')

    # --- Основной игровой цикл ---
    while True:
        if not error_counter < MAX_ERRORS:
            print('Вы проиграли!')
            write_answer_append(f'Игрок проиграл!', ANSWERS_FILEPATH)
            break  
        
        # --- Ход игрока ---
        user_city = input(f'Введите название города (осталось попыток: {MAX_ERRORS - error_counter}): ').lower()        
        if not validate_user_city(user_city, cities_list, current_city):
            error_counter += 1
            print('Неверное название города.')
            write_answer_append(f'Игрок назвал город с ошибкой: {error_counter} раз', ANSWERS_FILEPATH)
            continue
        current_city = user_city
        write_answer_append(f'Игрок назвал город: {current_city}', ANSWERS_FILEPATH)
        cities_list.remove(current_city)
        
        # --- Ход компьютера ---
        print('Ход компьютера ...')
        current_city = get_computer_city(get_last_char(current_city), cities_list)
        if not current_city:
            print('Вы выиграли!')
            write_answer_append(f'Компьютер не смог подобрать подходящий город. Игрок выиграл!', ANSWERS_FILEPATH)
            break
        print(f'Компьютер назвал город: {current_city}')
        write_answer_append(f'Компьютер назвал город: {current_city}', ANSWERS_FILEPATH)
        cities_list.remove(current_city)