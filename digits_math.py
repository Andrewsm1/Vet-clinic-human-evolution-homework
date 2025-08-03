# Получаем пятизначное число
number = int(input("Введите пятизначное число: "))

# Извлекаем нужные цифры
units = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
tens_thousands = (number // 10000) % 10

# Пошаговое вычисление
try:
    power = tens ** units
    product = power * hundreds
    difference = tens_thousands - thousands
    result = product / difference
    print(f"Результат: {float(result)}")
except ZeroDivisionError:
    print("Ошибка: деление на ноль. Разность десятков тысяч и тысяч равна 0.")