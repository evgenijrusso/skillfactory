# Выполним импорт из основного файла класса, где описан прямоугольник (Rectangle),
# «возьмём» оттуда все свойства, такие как width (ширина) и height (высота), и создадим «псевдо» прямоугольник r1.

from rectangle import Rectangle

r1 = Rectangle(10, 5)
print('r1.width: ', r1.width)
print('r1.heigth: ', r1.heigth)
print('r1.get_width: ', r1.get_width())
print('r1.get_heigth: ', r1.get_heigth())
print('r1.get_area: ', r1.get_area())

r2 = Rectangle(7, 4)
print('r2.width: ', r2.width)
print('r2.heigth: ', r2.heigth)
print('r2.get_width: ', r2.get_width())
print('r2.get_heigth: ', r2.get_heigth())
print('r2.get_area: ', r2.get_area())
