# Определение, встречалось ли число ранее

# Ввод строки чисел
numbers = list(map(int, input().split()))

# Множество для хранения уже встреченных чисел
seen = set()

# Обрабатываем каждое число
for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)