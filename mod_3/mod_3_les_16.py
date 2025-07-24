class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

class CarBody:
    def __init__(self, body_type, number_of_doors):
        self.body_type = body_type
        self.number_of_doors = number_of_doors

class Wheel:
    def __init__(self, diameter, type_of_rubber):
        self.diameter = diameter
        self.type_of_rubber = type_of_rubber

class Car:
    def __init__(self, engine, car_body, wheel):
        self.engine = engine
        self.car_body = car_body
        self.wheel = wheel

    def display_engine_info(self):
        print(f"Horsepower: {self.engine.horsepower} hp")
        print(f"Fuel type: {self.engine.fuel_type}")
        print()

    def display_car_body_info(self):
        print(f"Body type: {self.car_body.body_type}")
        print(f"Number of doors: {self.car_body.number_of_doors}")
        print()

    def display_wheel_info(self):
        print(f"Diameter: {self.wheel.diameter}")
        print(f"Type of rubber: {self.wheel.type_of_rubber}")
        print()


engine_1 = Engine(200, "Diesel")
car_body_1 = CarBody("SUV", 5)
wheel_1 = Wheel(18, "Winter")
car_1 = Car(engine_1, car_body_1, wheel_1)

car_1.display_engine_info()
car_1.display_car_body_info()
car_1.display_wheel_info()

engine_2 = Engine(500, "Diesel")
car_body_2 = CarBody("SUV", 3)
wheel_2 = Wheel(20, "Winter")
car_2 = Car(engine_2, car_body_2, wheel_2)

car_2.display_engine_info()
car_2.display_car_body_info()
car_2.display_wheel_info()