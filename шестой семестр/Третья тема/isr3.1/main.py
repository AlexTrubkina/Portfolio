"""

Автор: Трубкина А.Ю.

Разработать программу, позволяющую решать квадратное уравнение
через вычисление дискриминанта. В программе должен быть предусмотрен
ввод значений коэффициентов a, b, c пользователем. Требуется
протестировать программу с помощью одной из специальных библиотек.


"""
import math
def quad_eq():
    print("Введите коэффициенты для уравнения")
    print("ax^2 + bx + c = 0:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
 
    discr = diskriminant(a, b, c)
    res = solve(a, b, discr)
    return res

def diskriminant(a, b, c):
    if a == 0:
        return None
    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)
    return discr

def solve(a, b, discr):
    if discr == None:
        print("Деление на 0")
        return None
    if discr > 0:
        print("Дискриминант больше нуля. Два корня")
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        return [x1, x2]
    elif discr == 0:
        print("Дискриминант равен нулю. Один корень")
        x = -b / (2 * a)
        print("x = %.2f" % x)
        return x
    else:
        print("Дискриминант меньше нуля. Корней нет")
        return None





quad_eq()
