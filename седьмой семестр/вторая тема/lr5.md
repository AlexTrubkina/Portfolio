# Лабораторная работа № 5

Спарсить страницу https://www.herzen.spb.ru/main/structure/inst/ и создать json-файл со списком институтов, где структура файла будет такой: 

```json
[ {"institute_name":"", "url": "", 
  [
   {"dep_name": "кафедра", "head_name":"имя", "email":"почта"},
   ...
  ]}, 
 ...
]
```

дополнить файл с данными, организовав парсинг страниц институтов на сайте https://atlas.herzen.spb.ru/faculty.php. Спарсить список кафедр этого института и дополнить файл информацией о руководителях кафедр этого института: имя и почта. 

В качестве ответа приведите ссылку на Google Colab с кодом решения.

Базовый код: 

```py
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.herzen.spb.ru/main/structure/inst/')
bs = BeautifulSoup(html, "html.parser")
nameList = bs.find('td',{'class':'block'}).children
# nameList = bs.findAll('td', {'class': 'block'})
# for i in range(10) # for (let i=0; i < 10; i++) {}   
# for name in nameList:
#     print(name.get_text())
for child in nameList:
  print(child)
 ```
 
 [Отчет](https://colab.research.google.com/drive/13FDlgaJ9bFbkYZWNAsw5qhwS-1nl6-0D?usp=sharing)
