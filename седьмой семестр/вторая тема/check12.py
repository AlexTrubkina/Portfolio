"""
Дан Gist с текстом статьи сэра Тима Бернерса-Ли, оригинал тут: https://www.w3.org/DesignIssues/TimBook-old/History.html

Необходимо с использованием библиотеки nltk решить задачу частеречной разметки и найти 5 (пять) наиболее встречаемых частей речи в этом тексте.

В качестве ответа необходимо представить ссылку на Google Colab или на репозиторий GitHub (обозначьте ответы в README.md), в которой будет располагаться файл (ipynb или py) с выводом списка с обозначениями частей речи и количеством их в тексте.

Например:

Имя существительное - 123

Предлог - 456

Прилагательное - 789

Междометие - 89

Наречие - 42

Подсказка по алгоритму решешиня задачи:

Получить текст с помощью requests или urllib.request.
Преобразовать в utf-8.
Найти функцию для решения частеречной разметки.
Не забыть провести токенизацию текста перед разметкой.
Определить топ-5 частей речи и найти вывести их на экран в понятном виде.
"""

from urllib.request import urlopen
import nltk
from bs4 import BeautifulSoup

html = urlopen('https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt')
text = BeautifulSoup(html, "html.parser")
text = str(text)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
tokens = nltk.word_tokenize(text)
data = nltk.pos_tag(tokens)

from collections import Counter
counts = Counter(tag for word,tag in data)

# Считаю части речи

noun = counts['NNS'] + counts['NNP'] + counts['NN']
souz = counts['CC'] 
verb = counts['VB'] + counts['VBD'] + counts['VBG'] + counts['MD']
mestoim = counts['PRP'] + counts['VBP'] + counts['PRP'] + counts['VBZ'] + counts["WP"]
pril = counts['JJ'] + counts['JJS']

print('Имя существительное - ', noun)
print('Союз - ', souz)
print('Прилагательное - ', pril)
print('Глагол - ', verb)
print('Местоимение - ', mestoim)
