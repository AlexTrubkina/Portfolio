"""

Автор: Трубкина Александра 

группа 1.2 

Создание программы с реализацией вручную одного из алгоритмов сортировки (вставки, плавной сортировки).


"""

def main():
    mas = []
    n = int(input("Введите количесво элементов массива: ")) 
    print("Введите элементы массива:") 
    for i in range(n):  
        new_el = int(input())  # считываем очередной элемент
        mas.append(new_el)  
    print(mas)
    print("Отсортированный массив: ", sotr_insert(mas))

def sotr_insert(mas):
    for i in range(1, len(mas)):
        item = mas[i]
        j = i - 1
        while(j >= 0 and mas[j] > item):
            mas[j + 1] = mas[j]
            j -= 1
        mas[j + 1] = item
    return mas

main()
