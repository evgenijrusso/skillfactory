# C4.6. Создание собственных  структур

# Ранее нами были рассмотрены следующие структуры данных: массив, список, стек, очередь, \
# хеш-таблица (словарь), граф, дерево.

# Сейчас мы попробуем создать класс LinkedList, реализующий список.
# Элементы списка будут представлять собой экземпляры класса Node.


# Мы определили класс Node.
# Конструктор этого класса принимает значение элемента и ссылку на следующий элемент. По умолчанию они оба None.
# Также был определён метод __str__, который используется для строкового представления объекта.
class Node: # класс элемента
    def __init__(self, value=None, next_=None):  # инициализируем
        self.value = value # значением
        self.next = next_   # ссылкой на следующий элемент

    def __str__(self):
        return 'Node value = ' + str(self.value)

# Также был определён основной класс LinkedList.
# Конструктор метода инициализирует ссылки на первый и на последний элемент,
# а также определяется метод clear, который очищает список.
class LinkedList:  # класс списка
    def __init__(self): # инициализируем пустым
        self.first = None
        self.last = None

    def clear(self):
        self.__init__() # очищаем список

    def __str__(self): # функция печати
        R = ''
        pointer = self.first # берем 1-й указатель
        while pointer is not None: # пока указатель не станет None
            R += str(pointer.value) # добавляем значение в строку
            pointer = pointer.next  # идём дальше по указателю
            if pointer is not None:
                R += ' '
        return R

    def pushleft(self, value):
        if self.first == None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def pushright(self, value):
       if self.first == None:
           self.first = Node(value)
           self.last = self.first
       else:
           new_node = Node(value)
           self.last.next = new_node
           self.last = new_node


    def popleft(self):
        if self.first is None: # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first           # сохраняем его
            self.__init__()             # очищаем его
            return node               # и возвращаем сохранённый элемент
        else:
            node = self.first       # сохраняем первый элемент
            self.first = self.first.next   # меняем указатель на первый элемент
            return node                     # возвращаем сохранённый


    def popright(self):
        if self.first is None: # если список пустой, возвращаем None
            return None
        elif self.first == self.last:
            node = self.first  # сохраняем его
            self.__init__()  # очищаем его
            return node  # и возвращаем сохранённый элемент
        else:
            node = self.last   # сохраняем последний
            pointer = self.first # создаем указатель
            while pointer.next is not node:  # пока не найдём предпоследний
                pointer = pointer.next
            pointer.next = None    # обнуляем указатели, чтобы
            self.last = pointer   # предпоследний стал последним
            return node         # возвращаем сохранённый


    def __iter__(self): # объявляем класс как итератор
        self.current = self.first  # в текущий элемент помещаем первый
        return self

    def __next__(self):  # метод перехода
        if self.current is None:  # если текущий стал последним
            raise StopIteration  # вызываем исключение
        else:
            node = self.current # сохраняем текущий элемент
            self.current = self.current.next  # совершаем переход
            return node     # и возвращаем сохранённый

    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count


print('Задание 4.6.3')
LL = LinkedList()
print('pushright: ', LL.pushright(1))
print('pushleft: ', LL.pushleft(2))
print('pushright: ', LL.pushright(3))
print('popright: ', LL.popright())
print('pushleft: ', LL.pushleft(4))
print('pushright: ', LL.pushright(5))
print('popleft: ', LL.popleft())

print('LL:', LL)

print('LL:', LL.__len__())