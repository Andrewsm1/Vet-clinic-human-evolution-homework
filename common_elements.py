# Подсчёт количества чисел, которые есть в обоих списках

# Чтение первого списка (до пустой строки)
first_list = []
while True:
    try:
        line = input()
        if line == "":
            break
        first_list.append(int(line))
    except EOFError:
        break

# Остальное — второй список
second_list = []
while True:
    try:
        line = input()
        second_list.append(int(line))
    except EOFError:
        break

# Преобразуем в множества и ищем пересечение
common = set(first_list) & set(second_list)

# Выводим количество общих чисел
print(len(common))