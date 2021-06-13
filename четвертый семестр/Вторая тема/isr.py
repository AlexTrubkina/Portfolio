"""

Автор: Трубкина А. Ю.

Задание. 
2.1. Разработать прототип программы "Калькулятор", позволяющую выполнять базовые арифметические действия и функцию обертку, сохраняющую название выполняемой операции, аргументы и результат в файл.  [ без использования '@' ]



2.2. Дополнение программы "Калькулятор" декоратором, сохраняющим выполняемые действия, в файл-журнал. 

2.3. Рефакторинг (модификация) программы с декоратором модулем functools и использование его функционала.

2.4. Формирование отчета по практическому заданию и публикация его в портфолио.

"""

import functools
import json

def main():
    try:
        fnum = float(input("Введите первое число: "))
        snum = float(input("Введите первое число: "))
        operation = input("Выберите операцию (+, -, /, *): ")
        result = culc(fnum, snum, operation)
        print(result)
    except ValueError:
        print("Вы ввели не число")


def wrapper(func):
    @functools.wraps(func)
    def journal(num1, num2, operation):
        res = func(num1, num2, operation)
        writer = str(num1) + ' ' + str(operation) + ' ' + str(num2) + ' = ' + str(res) + '\n'
        try: 
            with open('journal.txt', 'w', newline='') as f:
                f.write(writer)     
        except FileNotFoundError as e:
            print("Something went wrong: ", e)  
            return None
        return res      
    return journal

@wrapper
def culc(num1, num2, operation = ""):
    try:
        if(operation == "+"):
            return num1 + num2
        elif(operation == "-"):
            return num1 - num2
        elif(operation == "*"):
            return num1 * num2
        elif(operation == "/"):
            return num1 / num2
        else:
            print("Нет такой операции")
            return None 
    except ArithmeticError as e:
        print("Error: ", e)



main()
    
