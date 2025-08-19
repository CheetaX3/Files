class MyDict:
    # Инициализация пустого словаря
    def __init__(self):
        self._data = {}

    # Получение значения по ключу, если нет — вернуть None
    def __getitem__(self, key):
        return self._data.get(key, None)

    # Установка значения по ключу
    def __setitem__(self, key, value):
        self._data[key] = value

    # Удаление элемента по ключу, если он существует
    def __delitem__(self, key):
        if key in self._data:
            del self._data[key]

    # Проверка наличия ключа
    def __contains__(self, key):
        return key in self._data
    
    # Возвращает список всех ключей
    def keys(self):
        return list(self._data.keys())

    # Возвращает список всех значений
    def values(self):
        return list(self._data.values())

    # Возвращает список пар (ключ, значение)
    def items(self):
        return list(self._data.items())

    # Возвращает строковое представление словаря
    def __str__(self):
        return str(self._data)


my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']