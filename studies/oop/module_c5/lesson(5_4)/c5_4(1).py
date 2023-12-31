import requests
import lxml.html
from lxml import etree

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser()) # попытаемся спарсить наш файл с помощью html-парсера.
# не стал копировать в папку, нашел в оригинале начало новостей  /html/body/div/div[3]/div/section/div[3]/div[1]/div/ul/li[1]

ul = tree.findall('/body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')  # li[1] в примере было li. p.s. убрать [1]
# помещаем в аргумент метода findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)

# создаём цикл, в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>.
    #print(a.text)   # из этого тега забираем текст, это и будет нашим названием
    time = li.find('time')
    print(time.get('datetime'),  a.text)

# Обратите внимание, что в скопированном из браузера xpath надо внести изменения.
# А конкретно: мы удалили начальный тег /HTML из поиска. В основном методы find и findall работают так же,
# как и функция xpath, но всё же есть отличия. Как вы догадались, findall возвращает список многих подходящих элементов,
# в то время как метод find возвращает только первый подходящий элемент.
# Также второй аргумент в функции .parse() обязательный.
# Без него мы парсить не сможем, потому как для восприятия парсером переданного в IDE HTML-текста,
# а не какого-либо ещё, нужно передать объект класса HTMLParser.
