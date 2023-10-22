from cat import Cat

cat_1 = Cat(name='Bood', age=5, gender='female')
cat_2 = Cat(name='Orly', age=2, gender='male')

print('Кот 1: ', cat_1.get_name(), cat_1.get_age(), cat_1.get_gender())
print('Кот 2: ', cat_2.get_name(), cat_2.get_age(), cat_2.get_gender())


class Dog(Cat):

    def get_pet(self):
        return f'{self.get_name()} {self.get_age()}'

dog_1 = Dog('Felox', 5, gender='male')
print(dog_1.get_pet())