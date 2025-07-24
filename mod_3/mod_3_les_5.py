class Rectangle:
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle: Width: {self.width}, Height: {self.height}'

    def calculate_area(self):
        return self.width * self.height

    def resize(self, width, height):
        self.width = width
        self.height = height

    def display_info(self):
        print(f"Rectangle: Width: {self.width}, Height: {self.height}, Area: {self.calculate_area()}")

rectangle1 = Rectangle(5, 10)
print(rectangle1)

rectangle2 = Rectangle(5, 10)
print(rectangle2)