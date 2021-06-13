"""

Автор: Трубкина Александра

группа 1.2

4.1. Создание программы по заполнению массивов случайными значениями. Сортировка значений в списке методом вставки, плавной сортировки, с помощью встроенных функций языка.

4.2. Создание программы по распределению списка с случайными значениями на два списка по определенному критерию (четность/нечетность, положительные/отрицательные числа).

"""

def main():
    mas_r = rand_mas()
    print("Исходный массив:\n", mas_r)
    mas = sotr_insert(mas_r)
    print("Отсортированный массив методом вставок:\n", mas)
    print("Рапределение списка на два: ")
    div_mas(mas)
    


# 4.1 Сортировка методом вставки

import random 

def rand_mas():
    mas = [] 
    for i in range(10):
        mas.append(random.randint(0, 100)) 
    return mas

def sotr_insert(mas):
    for i in range(len(mas)):
        item = mas[i]
        j = i - 1
        while(j >= 0 and mas[j] > item):
            mas[j + 1] = mas[j]
            j -= 1
        mas[j + 1] = item
    return mas

# 4.2 Функция делит массив на два массива с четными и нечетными числами

def div_mas(mas):
    mas1, mas2 = [], []
    for i in range(len(mas)):
        if(mas[i] % 2 == 0):
            mas1.append(mas[i])
        else:
            mas2.append(mas[i])
    print(mas1)
    print(mas2)


main()
