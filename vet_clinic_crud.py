import collections

# Изначальная "база данных"
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_suffix(age):
    """Склонение для слова 'год' по числу"""
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"

def get_pet(ID):
    """Получает питомца по ID, возвращает словарь или False"""
    return pets[ID] if ID in pets else False

def pets_list():
    """Выводит всех питомцев из базы"""
    for ID, pet_data in pets.items():
        for name, info in pet_data.items():
            suffix = get_suffix(info["Возраст питомца"])
            print(f'ID {ID} — Это {info["Вид питомца"]} по кличке "{name}". '
                  f'Возраст питомца: {info["Возраст питомца"]} {suffix}. '
                  f'Имя владельца: {info["Имя владельца"]}')

def create():
    """Добавляет нового питомца"""
    last = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last + 1

    name = input("Введите кличку питомца: ")
    kind = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")

    pets[new_id] = {
        name: {
            "Вид питомца": kind,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Питомец добавлен с ID: {new_id}")

def read():
    """Показать информацию о питомце по ID"""
    id_input = int(input("Введите ID питомца: "))
    pet_data = get_pet(id_input)
    if pet_data:
        for name, info in pet_data.items():
            suffix = get_suffix(info["Возраст питомца"])
            print(f'Это {info["Вид питомца"]} по кличке "{name}". '
                  f'Возраст питомца: {info["Возраст питомца"]} {suffix}. '
                  f'Имя владельца: {info["Имя владельца"]}')
    else:
        print("Питомец не найден.")

def update():
    """Обновить данные о питомце"""
    id_input = int(input("Введите ID питомца для обновления: "))
    pet_data = get_pet(id_input)
    if pet_data:
        for name in pet_data:
            print(f"Текущая кличка: {name}")
            new_name = input("Новая кличка: ")
            kind = input("Новый вид питомца: ")
            age = int(input("Новый возраст: "))
            owner = input("Новое имя владельца: ")
            pets[id_input] = {
                new_name: {
                    "Вид питомца": kind,
                    "Возраст питомца": age,
                    "Имя владельца": owner
                }
            }
            print("Данные обновлены.")
    else:
        print("Питомец не найден.")

def delete():
    """Удалить питомца по ID"""
    id_input = int(input("Введите ID питомца для удаления: "))
    if id_input in pets:
        del pets[id_input]
        print("Питомец удалён.")
    else:
        print("Питомец не найден.")

# Главный цикл программы
while True:
    print("\nКоманды: create, read, update, delete, list, stop")
    command = input("Введите команду: ").lower()

    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command == "stop":
        print("Выход из программы.")
        break
    else:
        print("Неизвестная команда.")