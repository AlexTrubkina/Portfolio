"""

Написать функцию squareSequenceDigit(), где решалась бы следующая задача. Найти n-ю цифру последовательности из квадратов целых чисел: 149162536496481100121144...

Например, 2-я цифра равна 4, 7-я 5, 12-я 6. Использовать операции со строками в этой задаче запрещается.

Протестировать выполнение программы со следующими значениями:

при вызове squareSequenceDigit(1) должно быть 1;
squareSequenceDigit(2) вернёт 4;
squareSequenceDigit(7) вернёт 5;
squareSequenceDigit(12) вернёт 6;
squareSequenceDigit(17) вернёт 0;
squareSequenceDigit(27) вернёт 9.

"""

import math

def length(x):
    # возвращает длину числа 
    lg = math.log(x, 10)
    result = math.floor(lg) + 1
    return result

def numOnPosition(x, n):
    # возвращает какая цифра стоит в числе х на позиции n
    k = 0 
    k = length(x) - n + 1 # обратная позиция
    return ((x - (x // pow(10, k)) * pow(10, k)) // pow(10, (k - 1)))
    # (x - (x // pow(10, k) - убирает разряды справа
    #  // pow(10, (k - 1)) - убирает разряды слева

def squareSequenceDigit(n):
    i, x, r, k = 0, 0, 0, 0
    i = 0
    r = -1
    while r < 0: 
        i = i + 1 # номер числа в ряду
        x = int(math.pow(i, 2)) # числа в ряду
        k = length(x) # длина числа в ряду
        if n > k:
            n = n - k # выкидываем число из ряда если n больше чем количество цифр в числе x 
        else:
            r = numOnPosition(x, n) # иначе искомая цифра в числе    
    result = r      
    return result
    
    
    
    
if __name__ == "__main__":
    squareSequenceDigit(1)
    squareSequenceDigit(2)
    squareSequenceDigit(7)
    squareSequenceDigit(12)
    squareSequenceDigit(17)
    squareSequenceDigit(27)
