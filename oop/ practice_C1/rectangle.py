class Rectangle:

    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def get_width(self):
        return self.width

    def get_heigth(self):
        return self.heigth

    def get_area(self):              # Метод, рассчитывающий площадь
        return self.width * self.heigth
