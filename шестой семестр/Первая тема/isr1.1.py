"""
Автор: Трубкина А.Ю.

Разработка скрипта, вычисляющего статистические показатели (среднее значение, дисперсия, среднее квадратичное отклонение) для данных, считанных из CSV-файла.

"""
import pandas

data = pandas.read_csv('data.csv', index_col="id")

def sr_znach():
    sumOfallAges = 0
    count = 0
    for i in data['age']:
        sumOfallAges += i
        count +=1
    sr = sumOfallAges / count
    print('Среднее значение: ', sr)
    return sr


sr = sr_znach()

def disp():
    delt, sqOfdelt, sumOfnum, num = 0, 0, 0, 0
    
    for i in data['age']:
        delt = i - sr 
        sqOfdelt = delt * delt
        sumOfnum += sqOfdelt
        num += 1

    dispOfages = sumOfnum / num
    print('Дисперсия: ', dispOfages)
    return dispOfages


disp = disp()

import math
def sr_otkl():
    res = math.sqrt(disp)
    print('Среднее квадратичное отклонение: ', res)
    return res

sr_otkl()
