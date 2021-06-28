"""
Автор: Трубкина А.Ю.

Создание пользовательского пакета для приложения «Гостевая книга» с
прототипами методов, позволяющих взаимодействовать с JSON-файлом
(создание, удаление, переименование, чтение, запись). Формирование отчета по практическому заданию и публикация его в портфолио.

"""

import json

def json_read():
    try:
        with open('example.json', 'r', encoding='utf-8') as f:
            data = f.read()
        return data
    except FileNotFoundError:
        print("Такого файла не существует!")

json_read()


def json_write():
    print('Впишите что вы хотите записать в файл:')
    age = input("Впишите возраст постояльца: ")
    name = input("Впишите имя постоятельца: ")
    surname = input("Впишите фамилию постояльца: ")
    ex_dict = {"name": "",  
              "age": "",  
              "surname": ""}
    ex_dict["age"] = age
    ex_dict["name"] = name
    ex_dict["surname"] = surname
    try:
        with open('example.json', 'w') as outfile:
            json.dump(ex_dict, outfile)
    except FileNotFoundError:
        print("Такого файла не существует!")

json_write()
