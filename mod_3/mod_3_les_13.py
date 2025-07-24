# Задание 1

class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        return f'Название: {self.title}; Автор: {self.author}; Год издания: {self.year}'

class Book(Publication):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}; Жанр: {self.genre}'

class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number
    
    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}; Номер выпуска: {self.issue_number}'

class Newspaper(Publication):
    def __init__(self, title, author, year, publisher):
        super().__init__(title, author, year)
        self.publisher = publisher

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}; Издатель: {self.publisher}'

book_1 = Book('Руслан и Людмила', 'А.С. Пушкин', 2010, 'Поэма')
magazine_1 = Magazine('Esquire', 'Дэвид Смарт, Генри Джексон и Арнольд Гингрич', 1933, 1)
newspaper_1 = Newspaper('USA Today', 'Эл Ньюхарт', 1982, 'Gannett Company')

print(book_1.get_info())
print(magazine_1.get_info())
print(newspaper_1.get_info())

# Задание 2

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f'Название: {self.name}; Цена: {self.price}'

class Product(Item):
    def __init__(self, name, price, brand, category):
        super().__init__(name, price)
        self.brand = brand
        self.category = category

    def get_brand(self):
        return self.brand

    def get_category(self):
        return self.category

class Food(Product):
    def __init__(self, name, price, brand, category, expiry_date, weight):
        super().__init__(name, price, brand, category)
        self.expiry_date = expiry_date
        self.weight = weight

    def get_expiry_date(self):
        return self.expiry_date

    def get_weight(self):
        return self.weight

class Beverage(Product):
    def __init__(self, name, price, brand, category, volume, carbonated):
        super().__init__(name, price, brand, category)
        self.volume = volume
        self.carbonated = carbonated

    def get_volume(self):
        return self.volume

    def is_carbonated(self):
        return self.carbonated

    
# Создание объектов класса Food
food1 = Food("Banana", 1.99, "Chiquita", "Fruit", "2023-01-31", 150)
food2 = Food("Cheese", 4.99, "Kraft", "Dairy", "2022-12-15", 250)

# Создание объектов класса Beverage
beverage1 = Beverage("Coca Cola", 2.49, "Coca Cola Company", "Soft Drink", 500, True)
beverage2 = Beverage("Water", 0.99, "Aquafina", "Bottled Water", 1000, False)

# Вызов методов для объектов класса Food
print(food1.get_info())  # Вывод: Name: Banana, Price: 1.99
print(food1.get_brand())  # Вывод: Chiquita
print(food1.get_expiry_date())  # Вывод: 2023-01-31

# Вызов методов для объектов класса Beverage
print(beverage2.get_info())  # Вывод: Name: Water, Price: 0.99
print(beverage2.get_brand())  # Вывод: Aquafina
print(beverage2.is_carbonated())  # Вывод: False