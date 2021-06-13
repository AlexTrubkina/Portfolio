"""

Реализовать программу-игру «Угадай число», в которой для вывода на экран информации использовать метод format.

"""

import random 

def main():
    f = 'y'
    while(f == 'y'):
        a = int(input('Введите нижнюю границу: '))
        b = int(input('Введите верхнюю границу: '))
        num = int(input('Введите искомое число: '))
        f = random.randrange(a, b, 1);
        search(num, f)
        print("Начать игру заново?(y/n)")
        f = input()

def search(num, finder):
    while num != finder:
        if num < finder:
            print("Число {} меньше чем искомое".format(str(num)))
            num = int(input('Введите искомое число: '))
        else: 
            print("Число {} больше чем искомое".format(str(num)))
            num = int(input('Введите искомое число: '))
    print("{} = {}".format(str(num), str(finder)))


main()
