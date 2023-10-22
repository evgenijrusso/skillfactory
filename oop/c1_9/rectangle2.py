from rectangle import Rectangle, Square, Circle

# далее создаём два прямоугольника

rest_1 = Rectangle(3, 5)
rest_2 = Rectangle(12, 5)

# вывод площади наших двух прямоугольников

print(rest_1.get_area(), rest_2.get_area())
print('a!=b', rest_1.a == rest_2.a)
print('a==b', rest_1.b == rest_2.b)
print('r1==r2', rest_1 == rest_2)

square_1 = Square(5)
square_2 = Square(7)

print(square_1.get_area_square(), square_2.get_area_square())

s1 = Circle(3)
s2 = Circle(7)
print('s:', s1.get_area_circle(), s2.get_area_circle())


# Теперь мы хотим в нашей программе все объекты перенести в единую коллекцию. Назовём фигуры (figures).
# Коллекция содержит список, в который и помещаем наш первый прямоугольник, квадрат

figures = [rest_1, rest_2, square_1, square_2, s1, s2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())


