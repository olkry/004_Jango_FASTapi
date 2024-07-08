# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
#
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.
#
# Примечание. Элементы главной диагонали также учитываются.


matrix = [[int(rows) for rows in input().split()] for _ in range(int(input()))]

maximum = matrix[0][0]

for r in range(len(matrix)):
    for c in range(r + 1):
        if maximum < matrix[r][c]:
            maximum = matrix[r][c]

print(maximum)

# +++++++++++++++++++++
n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

largest = matrix[0][0]

for i in range(n):
    for j in range(n):
        if i >= j and matrix[i][j] > largest:
            largest = matrix[i][j]

print(largest)
