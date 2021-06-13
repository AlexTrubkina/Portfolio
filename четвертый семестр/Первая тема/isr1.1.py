"""

Разработать программу с реализацией функции для считывания json-данных из файла и вывод их в табличном виде на экран. Реализовать базовый синтаксис для обработки исключений (try .. except)

"""


import json

def jsontolib():
    try:
        with open('myfile.json', 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                print(data)
                return data
            except json.decoder.JSONDecodeError as error:
                print("Файл пуст: ", error)
                return None
    except FileNotFoundError:
        print("Такого файла не существует!")
        return None

jsontolib()
