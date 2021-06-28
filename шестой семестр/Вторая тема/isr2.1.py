"""

Автор: Трубкина А.Ю.

На основе кода, предоставленного преподавателем, реализовать генератор
чисел ряда Фибоначчи. Генератор требуется создать двумя вариантами: с
помощью генератора списков, с помощью функции, внутри которой yield.

"""
class Fib:
    def __init__(self, max):
        self.max = max
        
        
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib
    
    
new_fib = Fib(0)
    
print(list(new_fib))

# c помощью генератора с yield
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
        
        
print(list(fibon(10)))
