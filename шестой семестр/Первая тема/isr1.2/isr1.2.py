"""
Автор: Трубкина А.Ю.

Осуществить рефакторинг (модификация) скрипта, вычисляющего
статистические показатели для данных, считанных из CSV, с использованием библиотеки научных вычислений numpy.

"""
import pandas
import numpy as np

data = pandas.read_csv('data.csv', index_col="id")
mass = data['age']

def sr_znach():
    sr = np.mean(mass)
    print('Среднее значение: ', sr)
    return sr

sr_znach()


def disp():
    dispOfages = np.var(mass)
    print('Дисперсия: ', dispOfages)
    return dispOfages

disp()
