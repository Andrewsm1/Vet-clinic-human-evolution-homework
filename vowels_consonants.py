# Получаем слово от пользователя
word = input("Введите слово (только маленькие латинские буквы): ")

# Списки гласных и согласных
vowels = "aeiou"
vowel_counts = {v: 0 for v in vowels}  # создаём словарь вида {'a': 0, 'e': 0, ...}

# Счётчики
vowel_total = 0
consonant_total = 0

# Перебираем буквы в слове
for letter in word:
    if letter in vowels:
        vowel_counts[letter] += 1
        vowel_total += 1
    else:
        consonant_total += 1

# Выводим общее количество
print("Количество гласных:", vowel_total)
print("Количество согласных:", consonant_total)

# Выводим количество каждой гласной
for v in vowels:
    if vowel_counts[v] > 0:
        print(f"{v}: {vowel_counts[v]}")
    else:
        print(f"{v}: False")