# Получение факториала и создание списка факториалов в убывающем порядке

import math

def get_factorial(n):
    """Возвращает факториал числа n"""
    return math.factorial(n)

# Ввод от пользователя
n = int(input("Введите натуральное число: "))

# Вычисляем факториалы от n до 1
factorial_list = [get_factorial(i) for i in range(n, 0, -1)]

# Выводим результат
print(factorial_list)