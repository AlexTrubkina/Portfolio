"""
Программа, считающая площадь треугольника по формуле Герона:

"""


def main():
    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
    c = float(input("Введите с: "))
    res = grn(a, b, c)
    print(res)

import math
def grn(a, b, c):
    """
    Расчет площади треугольника по формуле Герона
    """
    ppr = (a+b+c) / 2
    pl = pow(ppr * (ppr-a) * (ppr-b) * (ppr-c), 0.5)
    return pl

main()
