class DotTest:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_dot(self):
        return self.x, self.y

    def set_dot(self, val1, val2):
        try:
            self.x = val1
            self.y = val2
        except ValueError:
            raise ValueError("Pass an iterable with two items")
        else:
            return self.x, self.y

    # point = property(get_dot, set_dot(self=))
    @property
    def point(self):
        return self.x, self.y

    @point.setter
    def point(self, v1, v2):
        try:
            self.x = v1
            self.y = v2
        except ValueError:
            raise ValueError("Pass an iterable with two items")
        else:
            return self.x, self.y


d = DotTest(1, 2)
print('get_dot:', d.get_dot())
print('set_dot:', d.set_dot(4, 3))

print('point-get:', d.point)
lst = list(d.point)
lst[0] = 1
lst[1] = 5
p = tuple(lst)
print('point-set:', p)


print('dot_x: ', d.x)
print('dot_y: ', d.y)

point_test = (d.x, d.y)
print('point_test', point_test)
