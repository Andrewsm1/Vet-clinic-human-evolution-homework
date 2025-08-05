# Родительский класс
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Класс-наследник
class Autobus(Transport):
    pass  # Наследуем всё, ничего пока не добавляем

# Создаём объект
bus = Autobus("Renaul Logan", 180, 12)

# Выводим информацию
print(f"Название автомобиля: {bus.name} Скорость: {bus.max_speed} Пробег: {bus.mileage}")