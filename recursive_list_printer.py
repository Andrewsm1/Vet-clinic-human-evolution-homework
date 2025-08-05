# Исходный список
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Рекурсивная функция для вывода элементов списка
def print_list_recursive(lst, index=0):
    if index >= len(lst):  # Базовый случай: если индекс вышел за пределы
        print("Конец списка")
        return
    print(lst[index])  # Вывод текущего элемента
    print_list_recursive(lst, index + 1)  # Вызов функции для следующего элемента

# Запуск функции
print_list_recursive(my_list)