from abc import ABC, abstractmethod
from random import randint


class Person(ABC):

    def __init__(self, name, age, availability_of_money=0, having_your_own_home=False):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.having_your_own_home = having_your_own_home

    @abstractmethod
    def provide_information_about_yourself(self):
        raise NotImplementedError('This method is not implemented')

    @abstractmethod
    def make_money(self):
        raise NotImplementedError('This method is not implemented')

    @abstractmethod
    def buy_a_house(self):
        raise NotImplementedError('This method is not implemented')


class  Human(Person):

    def __init__(self, name, age, availability_of_money=0, having_your_own_home=False):
        super().__init__(name, age, availability_of_money, having_your_own_home)

    def provide_information_about_yourself(self):
        print(f'My name is {self.name} and I\'m {self.age}.')

    def make_money(self):
        make_money = randint(10000, 15000)
        self.availability_of_money += make_money
        print(f'{self.name} made {make_money}. Now {self.name}\'s balance is: {self.availability_of_money}')

    def buy_a_house(self, house):
        if self.availability_of_money >= house.cost and not house.is_sold:
            self.having_your_own_home = house
            self.availability_of_money -= house.cost
            self.having_your_own_home = True
            print(f'{self.name} bought a house')
        elif self.availability_of_money < house.cost:
            print(f'{self.name} doesn\'t have enough money for that :(')
        else:
            print(f'This house is already sold :(')


class House(ABC):

    def __init__(self, area, cost, id, is_sold):
        self.area = area
        self.cost = cost
        self.id = id
        self.is_sold = is_sold

    def __repr__(self):
        return f'House №{self.id}'


class Home(House):

    def __init__(self, area, cost, id, is_sold=False):
        super().__init__(area, cost, id, is_sold)


class RealtorMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):

    def __init__(self, name, houses, discount=False):
        self.name = name
        self.houses = houses
        self.discount = discount

    def provide_information_about_all_the_houses(self):
        [print(house) for house in self.houses]

    def give_a_discount(self):
        if self.discount:
            for house in self.houses:
                house.cost -= int(house.cost * self.discount / 100)

    def steal_your_money(self, human):
        if randint(0, 10) == 0:
            human.availability_of_money = 0


human1 = Human('John', 19)
human1.make_money()
human1.make_money()
human2 = Human('Garry', 25)
human2.make_money()
human2.make_money()
home1 = Home(10, 10000, 1, True)
home2 = Home(20, 20000, 2)
home3 = Home(30, 30000, 3)
realtor = Realtor('Mike', [home1, home2, home3], 10)
realtor.provide_information_about_all_the_houses()
human1.buy_a_house(home1)
realtor.steal_your_money(human1)
human2.buy_a_house(home2)
