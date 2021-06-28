"""

Автор: Трубкина А.Ю.

Разработать фрагмент программы, позволяющий получать данные о
текущих курсах валют с сайта Центробанка РФ с использованием сервиса,
который они предоставляют. Применить шаблон проектирования
«Одиночка» для предотвращения отправки избыточных запросов к серверу
ЦБ РФ. Оформить решение в виде корректно работающего приложения,
реализовать тестирование и опубликовать его в портфолио.

"""



import urllib.request

url = "http://www.cbr.ru/scripts/XML_daily.asp"

UrlSplit = url.split("/")[-1]

webFile = urllib.request.urlopen(url)
data = webFile.read()

ExtSplit = UrlSplit.split(".")[1]
FileName = UrlSplit.replace(ExtSplit, "xml")

with open(FileName, "wb") as localFile:
    localFile.write(data)


webFile.close()
