"""

Разработать фрагмент программы, который будет сохранять вводимые пользователем данные, по выбору в json, или csv-файле (использовать модули csv, json) с использованием протокола менеджеров контекста, а также расширенного синтаксиса исключений.

"""

def main():
    con = "y"
    namesAndSurnames = []
    while(con == "y"):
        firstName = input("Введите свое имя: ")
        surname = input("Введите свою фамилию: ")
        dataofuser = {"firstname": firstName,"surname": surname}
        namesAndSurnames.append(dataofuser)
        con = input("Хотели бы вы продолжить вводить данные? (y/n)")
    dictForData = {"members": namesAndSurnames}
    inputInFile(dictForData)


import json
def inputInFile(*data): 
    try:
        with open('example.json', 'w') as f:
            try:
                json.dump(data, f, sort_keys=True, indent=2)
                print("Данные записаны")
            except json.Error as e:
                print("Что-то пошло не так", e)
                return None
    except FileNotFoundError as e:
        print("Такого файла не существует ", e)
        return None

main()
