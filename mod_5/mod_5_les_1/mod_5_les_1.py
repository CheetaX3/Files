import string

def get_words(filename: str) -> list:
    with open(filename, 'r', encoding='utf8') as f:
        words = f.read().lower().translate(str.maketrans('', '', string.punctuation)).split()
    return words

def get_words_dict(words):
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1
    return words_dict

def main():
    filename = input('Введите имя файла: ')
    words = get_words(f'{filename}.txt')
    words_dict = get_words_dict(words)
    print(f'Количество слов в файле: {len(words)}')
    print(f'Количество уникальных слов в файле: {len(words_dict)}')
    print('Статистика по словам:')
    for word, count in words_dict.items():
        print(f' - {word} - {count} раз')
    
main()