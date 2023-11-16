# C3.2. Тонкости обработки исключений. Собственные классы исключений
# дерево стандартных исключений.

# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#   	+-- StopIteration
#   	+-- StopAsyncIteration
#   	+-- ArithmeticError
#   	|	FloatingPointError
#   	|	OverflowError
#   	|	ZeroDivisionError
#   	+-- AssertionError
#   	+-- AttributeError
#   	+-- BufferError
#   	+-- EOFError
#   	+-- ImportError
#   	|	+-- ModuleNotFoundError
#   	+-- LookupError
#   	|	+-- IndexError
#   	|	+-- KeyError
#   	+-- MemoryError
#   	+-- NameError
#   	|	+-- UnboundLocalError
#   	+-- OSError
#   	|	+-- BlockingIOError
#   	|	+-- ChildProcessError
#   	|	+-- ConnectionError
#   	|	|	+-- BrokenPipeError
#   	|	|	+-- ConnectionAbortedError
#   	|	|	+-- ConnectionRefusedError
#   	|	|	+-- ConnectionResetError
#   	|	+-- FileExistsError
#   	|	+-- FileNotFoundError
#   	|	+-- InterruptedError
#   	|	+-- IsADirectoryError
#   	|	+-- NotADirectoryError
#   	|	+-- PermissionError
#   	|	+-- ProcessLookupError
#   	|	+-- TimeoutError
#   	+-- ReferenceError
#   	+-- RuntimeError
#   	|	+-- NotImplementedError
#   	|	+-- RecursionError
#   	+-- SyntaxError
#   	|	+-- IndentationError
#   	|     	+-- TabError
#   	+-- SystemError
#   	+-- TypeError
#   	+-- ValueError
#   	|	+-- UnicodeError
#   	|     	+-- UnicodeDecodeError
#   	|     	+-- UnicodeEncodeError
#   	|     	+-- UnicodeTranslateError
#   	+-- Warning
#        	+-- DeprecationWarning
#        	+-- PendingDeprecationWarning
#        	+-- RuntimeWarning
#        	+-- SyntaxWarning
#        	+-- UserWarning
#        	+-- FutureWarning
#        	+-- ImportWarning
#        	+-- UnicodeWarning
#        	+-- BytesWarning
#        	+-- ResourceWarning

# Исключения классов SystemExit, KeyboardInterrupt, GeneratorExit не сигнализируют об ошибках.
# Эти исключения используют, чтобы сообщить о завершении работы кода (SystemExit),
# о нажатии клавиши прерывания (KeyboardInterrupt) или о закрытии генератора (GeneratorExit).

# Принято, что об ошибках сигнализируют объекты класса Exception и его потомков — с ними мы и будем работать

try:
    raise ZeroDivisionError  # возбуждаем исключение ZeroDivisionError
except ArithmeticError:  # ловим его родителя
    print("Hello from arithmetic error")

try:
    raise ZeroDivisionError
except ZeroDivisionError:  # сначала пытаемся поймать наследника
    print("Zero division error")
except ArithmeticError:  # потом ловим родителя
    print("Arithmetic error")


# Принцип написания и отлова собственного исключения следующий:

class MyException(Exception):  # создаём пустой класс – исключения
    pass


try:
    raise MyException("message")  # поднимаем наше исключение
except MyException as e:  # ловим его за хвост как шкодливого котёнка
    print(e)  # выводим информацию об исключении

# Давайте теперь попробуем построить собственные исключения с наследованием:
class ParentException(Exception):  # создаём пустой класс – исключения потомка, наследуемся от exception
    pass


class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
    pass


try:
    raise ChildException("message")  # поднимаем исключение-наследник
except ParentException as e:  # ловим его родителя
    print(e)  # выводим информацию об исключении

# Кстати говоря, класс с самописным исключением необязательно должен быть пустым.
# Если вы хотите добавить собственные аргументы в конструктор, дополнительно произвести какие-либо операции,
# то можете спокойно это делать, главное — не забыть о нескольких нюансах:

class ParentException(Exception):
    def __init__(self, message, error): # допишем к нашему пустому классу конструктор, который будет печатать дополнительно в консоль информацию об ошибке.
        super().__init__(message) # помним про вызов конструктора родительского класса
        print(f'Errors: {error}')

class ChildException(ParentException): # создаём пустой класс – исключение наследника, наследуемся от ParentException
    def __init__(self, messsge, error):
        super().__init__(messsge, error)

try:
    raise ChildException('message', 'error')
except ParentException as e:  # поднимаем исключение-наследник, передаём дополнительный аргумент
    print(e) # # выводим информацию об исключении

# Создать класс Square. Добавить в конструктор класса Square собственное исключение NonPositiveDigitException,
# унаследованное от ValueError, которое будет срабатывать каждый раз, когда сторона квадрата меньше или равна 0.

class NonPositiveDigitException(ValueError):
    pass
class Square:

    def __init__(self, a, mess='Неправильно указана сторона квадрата'):
        self.mess = mess
        if a <= 0:
            raise NonPositiveDigitException(self.mess)
        self.a = a
    @property
    def get_area_square(self):
        return self.a ** 2


s1 = Square(3)
print('sq: ', s1.get_area_square)
s2 = Square(0)


