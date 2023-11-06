#  конструктор класса, магический метод __init__, который заранее определяет атрибуты новых экземпляров.
#  Первым аргументом он обязательно принимает на вход self,
#  а дальше — произвольный набор аргументов, как обычная функция:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

peter = User(name="Peter Robertson", email="peterrobertson@mail.com")
julia = User(name="Julia Donaldson", email="juliadonaldson@mail.com")

print(peter.name, ' ', peter.email)
print(julia.name, ' ', julia.email)