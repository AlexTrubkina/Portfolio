"""
Автор: Трубкина А.Ю.

Дополните файл с кодом функции integrate, и также проведите замеры времени вычисления для аналогичных параметров модуля timeit для кратного числа потоков и процессов (2, 4, 6). Замеры вычислений - только для количества итераций n_iter=10**6

"""


import math
from concurrent.futures import as_completed
from functools import partial


def integrate(f, a, b, *, n_iter=10**6):
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
    # print(I)
    return I


import timeit

t_100 = timeit.timeit('integrate(lambda x: (x**2 + 3) / x, 1, 2)', "from __main__ import integrate", number = 10)

print("----simple integrate----")
print(t_100)
print("----simple integrate----")


from concurrent.futures import ThreadPoolExecutor
from functools import partial
from concurrent.futures import as_completed

def integrate_async(f, a, b, *, n_jobs=2, n_iter=10**6):

    # из futures необходимо импортировать классы для использования потоков и процессов, и оценить время выполнения интегрирования
    # с их помощью.
    # Используйте высокоуровневые классы для этого, см.
    # https://docs.python.org/3/library/concurrent.futures.html
    # в этом месте необходимо создать объекты этих классов, при этом количество потоков/процессов равняется количеству n_jobs.

    executor = ThreadPoolExecutor(n_jobs)    

    spawn = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)
    step = (b - a) / n_jobs
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    # print(sum(f.result() for f in as_completed(fs)))
    return sum(f.result() for f in as_completed(fs))

integrate_async(lambda x: (x**2 + 3) / x, 1, 2)

t_101 = timeit.timeit('integrate_async(lambda x: (x**2 + 3) / x, 1, 2)', "from __main__ import integrate_async", number = 10)

print("----integrate_async----")
print(t_101)
print("----sintegrate_async----")
