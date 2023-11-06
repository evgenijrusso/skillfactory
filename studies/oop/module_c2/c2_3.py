# C2.3. Декораторы класса: @property, @classmethod. Ещё пару слов о нашей бывшей возлюбленной — инкапсуляции
# Ну и напоследок стоит сказать пару слов о декораторе @classmethod, который встречается довольно редко,
# ввиду его малой понятности для обывателей и синтаксической громоздкости.

class ParentClass:
    @classmethod
    def method(cls, arg):
        print("%s clsssmethod. %d" % (cls.__name__, arg))

    @classmethod
    def call_original_method(cls):
        cls.method(5)

    def call_class_method(self):  # для объекта
        self.method(10)


class ChildClass(ParentClass):
    @classmethod
    def call_class_method(cls):
        cls.method(7)

# Вызываем методы класса через класс.
ParentClass.method(0)
ParentClass.call_original_method()
# ParentClass.call_class_method()  его нельзя так использовать!
ChildClass.method(0)
ChildClass.call_original_method()

# Вызываем методы класса через объект.
my_obj = ParentClass()
my_obj.method(1)  # ParentClassclassmethod. 1
my_obj.call_class_method()  # ParentClassclassme