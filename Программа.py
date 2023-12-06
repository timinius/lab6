#Метод анализа иерархий Томаса Саати

import numpy as np
import pandas as pd

# Вводим количество критериев
print('Сколько критериев Вы желаете рассмотреть?\n', 'Введите количество: ')
number = int(input())

def matrix(num):
    M = np.ones([num, num]) # Создаем матрицу
    for i in range(0, num):
        for j in range(0, num):
            if i < j:
                print('\nНасколько критерий', str(i+1), 'приоритетнее критерия', str(j+1), '?\n', 'Введите коэффициент: ')
                matrixij = input()
                M[i, j] = float(matrixij)
                M[j, i] = 1 / float(matrixij)  # Добавление обратных элементов (под главной диагональю)

    v = np.linalg.eig(M)[1][:, 0] # Вычисляем собственный вектор матрицы М.

    nv = v / v.sum() # Нормируем вектор
    return nv

nv = matrix(number)
# выводим результат
for x in range(len(nv)):
    res = list(str(nv[x]))
    res = res[1] + res[2] + res[3] + res[4]
    print(f'Коэффициент критерия', x+1, ':', res) # округление до сотых