import lxml.html
from lxml import etree

tree = etree.parse('c5_4_3.html', lxml.html.HTMLParser())
tag2 = tree.xpath('/html/body/tag1/tag2/text()')
print('tree:', tree)
print('tag2 text:', tag2)


#  ---------------  второе решение  ---------------------

# import lxml.html

html = ''' <html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>
'''

# tree = lxml.html.document_fromstring(html)
# text = tree.xpath('/html/body/tag1/tag2/text()')
# print(text)