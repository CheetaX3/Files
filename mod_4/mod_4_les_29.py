class MyDict:
    def __init__(self):
        self._data = []  # список пар [ключ, значение]

    def __getitem__(self, key):
        for k, v in self._data:
            if k == key:
                return v
        return None

    def __setitem__(self, key, value):
        for pair in self._data:
            if pair[0] == key:
                pair[1] = value
                return
        self._data.append([key, value])

    def __delitem__(self, key):
        for i, (k, v) in enumerate(self._data):
            if k == key:
                del self._data[i]
                return
   
    def __contains__(self, key):
        return any(k == key for k, _ in self._data)

    def keys(self):
        return [k for k, _ in self._data]

    def values(self):
        return [v for _, v in self._data]

    def items(self):
        return [(k, v) for k, v in self._data]

    def __str__(self):
        # превращаем список пар в строку в формате словаря
        return "{" + ", ".join(f"{repr(k)}: {repr(v)}" for k, v in self._data) + "}"


my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
print(my_dict)