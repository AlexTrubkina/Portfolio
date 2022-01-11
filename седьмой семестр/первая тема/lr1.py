"""

Автор: Трубкина А.Ю.

Написание программы для численного интегрирования площади под кривой. 

а и b - диапазон интегрирования
f - функция (например, sin, cos, tan, ...)
может быть любая функция из библиотеки math

"""



import math

def integrate(f, a, b, n_iter = 1000):
    # float  с точностью 10^-8
    # метод прямоугольников
    sum = 0.0
    h = (b - a) / n_iter
    x = a
    while (x <= b - h):
        sum += f(x)
        x += h
    I = h * sum
    I = round(I, 8)
    print(I)
    return I


if __name__ == '__main__':
    assert integrate(math.sin, 1, 2) == 0.95641515, "Should be 0.95641515"
    assert integrate(math.cos, 1, 2) == 0.06830466, "Should be 0.06830466"
    assert integrate(lambda x: (x**2 + 3) / x, 1, 2) == 3.57969173, "Should be 3.57969173"
   

