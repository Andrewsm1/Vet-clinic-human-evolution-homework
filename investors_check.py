# Получаем данные от пользователя
X = int(input("Введите минимальную сумму инвестиций (X): "))
A = int(input("Сколько у Майкла (A): "))
B = int(input("Сколько у Ивана (B): "))

# Проверяем условия
if A >= X and B >= X:
    print(2)
elif A >= X:
    print("Mike")
elif B >= X:
    print("Ivan")
elif A + B >= X:
    print(1)
else:
    print(0)