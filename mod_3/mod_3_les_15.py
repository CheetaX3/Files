import math
import doctest

class WinDoor:
    """
    Класс для описания окон и дверей
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Создание универсального объекта окна или двери

        :param x: float: длина окна/двери в метрах
        :param y: float: ширина окна/двери в метрах
        :return: None
        """
        self.square = x * y

class Room:
    """
    Класс для описания комнаты
    """
    def __init__(self, x: float, y: float, z: float) -> None:
        """
        Создание универсального объекта комнаты

        :param x: float: длина комнаты в метрах
        :param y: float: ширина комнаты в метрах
        :param z: float: высота комнаты в метрах
        :return: None
        """
        self.x = x
        self.y = y
        self.z = z
        self.wd = []
 
    def add_wd(self, w: float, h: float) -> None:
        """
        Добавление окон и дверей

        :param w: float: ширина в метрах
        :param h: float: длина в метрах
        :return: None
        """
        self.wd.append(WinDoor(w, h))

    def wall_surface(self) -> float:
        """
        Определение площади стен комнаты

        :return: float
        """
        return 2 * self.z * (self.x + self.y)
    
    def work_surface(self) -> float:
        """
        Определение рабочей площади комнаты

        :return: float
        """
        total_square = self.wall_surface()
        for wd in self.wd:
            total_square -= wd.square
        return total_square

    def wallpapers(self, w: float, h: float) -> int:
        """
        Определение количества обоев

        :param w: float: ширина рулона в метрах
        :param h: float: длина рулона в метрах
        :return: int
        """
        return math.ceil(self.work_surface() / (w * h))

doctest.testmod()

# print("Введите длинну, ширину и высоту комнаты в метрах")
# a = float(input("Длина: "))
# b = float(input("Ширина: "))
# c = float(input("Высота: "))
# r1 = Room(a, b, c)
# print(f"Площадь стен комнаты {r1.wall_surface()} метров")

# print("Введите ширину, высоту и количество окон")
# window_w = float(input("Ширина: "))
# window_h = float(input("Высота: "))
# window_n = int(input("Количество окон: "))
# for i in range(window_n):
#     r1.add_wd(window_w, window_h)

# print("Введите ширину, высоту и количество дверей")
# door_w = float(input("Ширина: "))
# door_h = float(input("Высота: "))
# door_n = int(input("Количество дверей: "))
# for i in range(door_n):
#     r1.add_wd(door_w, door_h)

# print("Введите ширину и длину рулона обоев")
# wallpaper_w = float(input("Ширина: "))
# wallpaper_h = float(input("Длина: "))

# print(f"Площадь комнаты для оклейки обоями {r1.work_surface()} метров")
# print(f"Количество рулонов обоев {r1.wallpapers(wallpaper_w, wallpaper_h)}")