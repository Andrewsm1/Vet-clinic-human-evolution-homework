import random  # Подключаем модуль random

# Функция для генерации матрицы заданного размера
def generate_matrix(rows, cols, min_value=-150, max_value=150):
    matrix = []
    for _ in range(rows):
        row = [random.randint(min_value, max_value) for _ in range(cols)]
        matrix.append(row)
    return matrix

# Функция для сложения двух матриц
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

# Функция для красивого вывода матрицы
def print_matrix(matrix, title="Матрица"):
    print(f"\n{title}:")
    for row in matrix:
        print(row)

# Пример: задаём размер матрицы
rows = 10
cols = 10

# Генерируем две матрицы
matrix_1 = generate_matrix(rows, cols)
matrix_2 = generate_matrix(rows, cols)

# Складываем их
matrix_sum = add_matrices(matrix_1, matrix_2)

# Выводим результат
print_matrix(matrix_1, "Матрица 1")
print_matrix(matrix_2, "Матрица 2")
print_matrix(matrix_sum, "Сумма матриц")