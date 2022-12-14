import doctest

class Laptop ():   # TODO Написать 3 класса с документацией и аннотацией типов
    def __init__(self, weight: int, battery: int):
        "Главные свойства при выборе ноутбука для постоянной переноски"
        if not isinstance (weight, int):
            raise TypeError ("Вес должен быть обозначен в числовом значении")
        self.weight = weight
        if weight >= 3:
            raise TypeError ("Ноубук тяжелее 3 кг не подходит для постоянной переноски")
        if not isinstance (battery, int):
            raise TypeError ("Объем аккумулятора должен быть обозначен в числовом значении")
        self.battery = battery
        if battery <= 4000:
            raise TypeError ("Объем аккумулятора слишком мал, для работы без возможности подлючения к разетке")
    def buy (self):
        "покупаем ноутбук"
        print("Модель ноутбука" + self.weight + "c общим весом" + self.battery + "и объемом аккамулятора подходит для покупки.")

class Smartphone:
    def __init__(self, screen_size: float, memory_capacity: str):
        "Ключевые параметры для покупки смартфона, для активно человека проводящего в нем много времени и активно ведущего социальные сети"
        if not isinstance (screen_size, float):
            raise TypeError ("Размер экрана должен быть написан в типе float")
        self.screen_size = screen_size
        if 5 <= screen_size <= 7:
            raise TypeError ("Данный размер экрана не подходит")
        if not isinstance (memory_capacity, str):
            raise TypeError ("Объем памяти должен быть написан в типе str")
        self.memory_capacity = memory_capacity
        if 64 <= memory_capacity <= 512:
            raise TypeError ("Данный объем памяти не подходит")
    def buy (self):
        print("Модель телефона" + self.screen_size + "с размером экрана" + self.memory_capacity + "и объемом памяти подходит для покупки")

class TV:
    def __init__(self, screen_size: str, resolution: str):
        if not isinstance(screen_size, str):
            raise TypeError ("Напишите необходимый размер экрана в типе str")
        self.screen_size = screen_size
        if 30 <= screen_size <= 100:
            raise TypeError("Данный размер экрана не подходит")
        if not isinstance(resolution, str):
            raise TypeError ("Напишите необходимое разрешение экрана в типе str")
        self.resolution = resolution
        if 4000 <= resolution <= 8000:
            raise TypeError ("Данное разрешение не подходит")
    def buy (self):
        print("Модель телевизора" + self.screen_size + "с размером экрана" + self.resolution + "и разрешением подходит для покупки" )

if __name__ == "__main__":
    Asus = Laptop (4, 5600)
    HP = Laptop (2, 4500)
    Samsung = Smartphone (6.5, 256)
    Iphone = Smartphone (4.5, 32)
    DEXP = TV (47, 2000)
    Sony = TV (50, 4000)

    doctest.testmod()
    pass
