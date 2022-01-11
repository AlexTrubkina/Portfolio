"""
Автор: Трубкина А.Ю.

Перемножение матриц
"""


fa = int(input('Введите количество строк первой матрицы: '))
fb = int(input('Введите количество столбцов первой матрицы: '))
sa = int(input('Введите количество строк второй матрицы: '))
sb = int(input('Введите количество столбцов второй матрицы: '))

fmatrix = [[0 for i in range(fb)] for j in range(fa)]
smatrix = [[0 for i in range(sb)] for j in range(sa)]


print('Введите значения первой матрицы:')

for i in range(len(fmatrix)):
    for j in range(len(fmatrix[i])):
        fmatrix[i][j] = int(input("Значение элемента: "))

print(fmatrix)

print('Введите значения второй матрицы:')

for i in range(len(smatrix)):
    for j in range(len(smatrix[i])):
        smatrix[i][j] = int(input("Значение элемента: "))

print(smatrix)

res = [[0 for i in range(fa)] for j in range(sb)]

if (fb == sa):
    for i in range(len(res)):
        for j in range(len(res[i])):
            for k in range(len(fmatrix[i])):
                res[i][j] += fmatrix[i][k] * smatrix[k][j]
else:
    print("Размерности матриц не подходят!")

print(res)
