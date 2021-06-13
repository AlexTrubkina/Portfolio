"""

Создание скрипта для считывания данных справочных логов из текстового файла и преобразования их в CSV-формат с последующей записью в новый файл. Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории.

"""

import json
with open('MOCK_DATA.json', 'r', encoding='utf-8') as f: #открываем файл на чтение
     data = json.load(f)
#print(data)

import csv
with open('answer.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
