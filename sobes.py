# import copy
#
#
# a = [i for i in range(5) if i % 2 == 0]
# a.append([])
# a[3].append(3)
#
#
# b = copy.deepcopy(a)
#
# a.append(4)
# print(a, b)
# print(a, b)
#
#
# a = 1
# def outer():
#     b = 1
#
#     def inner():
#         global a
#         a = 2
#         nonlocal b
#         b = 2
#         print(a, b)
#
#
#     inner()
#     print(a, b)
#
# outer()
# def chet(a):
#     if a % 2 == 0:
#         return a
#     else:
#         pass
#
#
# a = [i for i in range(5)]
# b = map(chet, [i for i in range(5)])
# print(list(b))
#
# a = [i for i in range(5)]
# b = list(map(lambda x: x*x, a))
# print(b)
#
#
# b = filter(lambda x: x % 2 == 0, a)
# print(list(b))
#
# a = [1, 2, 3]
# b = ['q', 'w', 'r']
#
# print('zip')
# c = zip(a, b)
# print(list(c))
#
#
#
# a = [1, 2, 3, 4, 1]
# print(a)
# a = tuple(a)
# print(a)
# a = set(a)
# print(a)
# a = {
#     1: 3,
#     2: 2,
#     3: 1
# }
#
# print(max(a, key=lambda x: a[x]))
#
#
# class Person:
#     work_plase = 'room'
#
#     @classmethod
#     def get_work_place(cls):
#         return cls.work_plase
#
# print(Person.get_work_place())
#
# from datetime import datetime
# class A:
#
#     @staticmethod
#     def get_current_datetime():
#         return datetime.now()
#
# print(A.get_current_datetime())

# from datetime import datetime
# a = (i for i in range(10000))
# b = [i for i in range(10000)]
# c = {i for i in range(10000)}
#
# print(a, b, c)
# def time_decorator(func):
#
#     def new_func(*args, **kwargs):
#         start = datetime.now()
#         func(*args, **kwargs)
#         stop = datetime.now()
#         print(stop-start)
#     return new_func
# @time_decorator
# def check_in(some, element):
#     if element in some:
#         return True
#     else:
#         return False
#
#
# print('start')
#
# print('-------------')
# check_in(some=b, element=1)
# check_in(some=b, element=1)
# print('-------------')
# check_in(some=c, element=1)
# print('-------------')
# check_in(some=a, element=1)
# print('start')
# check_in(some=a, element=1)
# print('111')
# check_in(some=b, element=1)
#
#
# def time_new_decorator(func):
#     def new_func(*args, **kwargs):
#         print('start decorator')
#         func(*args, **kwargs)
#         print('end decorator')
#     return new_func
# @time_new_decorator
# def some_funk(some_str: str):
#     print(f'{some_str}')
#
# some_funk('funk_1')


# from collections import OrderedDict, defaultdict, namedtuple
# import collections
#
# first = {1: 1, 2: 2}
# second = {2: 2, 1: 1}
# print(first==second)
#
#
# order_1 = OrderedDict(first)
# order_2 = OrderedDict(second)
# print(order_1 == order_2)
#
#
# title = namedtuple('worker', 'name age mabile_phone')
# db_1 = title('Ivan', '35', '+375292819815')
# print(db_1)
#
# print(collections.__all__)


# a = [1, 2, 3, 4]
# i = iter(a)
#
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# Эта строка уже вызывает ошибку, так ка мы вызываем элемент котого нет в списке# print(next(i))

# class Couter:
#     current: int
#
#     def __init__(self):
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         current = self.current
#         self.current += 1
#         return current
#
# c = Couter()
# i = iter(c)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
#
# # for i in c:
# #     print(i)
#
#
# def some():
#     yield 1
#
# b = some()
# print(next(b))
#
#
# try:
#     b = some()
#     print(next(b))
#     print(next(b))
# except:
#     print('1111')
# finally:
#     print('func is stopped')
# a = []
# if len(a)== 0:
#     print('stop')
# for i in a:
#     print(i)

# class Cat:
#     breed = 'british'
#     def __init__(self, name='cat', age=35):
#         self.name = name
#         self.age = age
#
#
#     def hellow(*args):
#         print('Hi in class cat', args)
#
#     def show_breed(self):
#         print(f'my cat is {self.breed}')
#
#     def check_the_name(self):
#         if hasattr(self):
#             print(f'that cat has name {self.name}')
#         else:
#             print('that cat have no name')
#
#

# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         print(f'{self.name} is {self.age} years old')
#
#     def speake(self):
#         print(f'{self.name} say gav')
#
# a = Dog('bob', 32)
# a.description()
# a.speake()

# mono sostoyanie
# class BestCar():
#     __shared_dict = {
#         'marks': 'reno',
#         'age': 5
#     }
#
#     def __init__(self):
#         self.__dict__ = self.__shared_dict

#
# class BankAccount():
#
#     def __init__(self, name, check,  balance):
#         self.__name = name
#         self.__check = check
#         self.__balance = balance
#
#     # def print_data(self):
#     #     return self.name, self.balance, self.check
#
#     def print_data(self):
#         return self.__name, self.__balance, self.__check
#
# bob = BankAccount('bob', 'dfsdfdff2655465465gfgfg10000', 10000)
# print(bob.print_data())
# print(bob.__dict__)
#
# class Universuti():
#
#     def __init__(self, name, age, branch):
#         self.name = name
#         self.age = age
#         self.branch = branch
#
#     def __print_data(self):
#         return self.name, self.age, self.branch
#
#     def acsees_to_priver_method(self):
#         return self.__print_data()
#
# bob = Universuti('bob', 35, 'PGS')
# print(bob.acsees_to_priver_method())

#
# class BancAccount():
#
#     def __init__(self, name, balance):
#         self.__name = name
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def set_balance(self, value):
#         self.__balance = value
#
# bob = BancAccount('Bob', 1000)
# print(bob.get_balance())
# print(bob.set_balance(2000))
# print(bob.get_balance())

# class Rectangle():
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
#     @property
#     def area(self):
#         return self.a * self.b
#
# r1 = Rectangle(3, 5)
# r2 = Rectangle(6, 1)
#
# print(r1.area)
# print(r2.area)

# class FoundLostInt():
#
#     __shared_dict = {
#         'same_int': 5,
#     }
#
#     def __init__(self):
#         self.__dict__ = self.__shared_dict
#
#     @staticmethod
#     def say_hellow():
#         print('Hi, the game is began')
#
# FoundLostInt.say_hellow()
# a = FoundLostInt()
# a.say_hellow()

# class StaticClass:
#
#     @staticmethod
#     def print_same_start():
#         return "start"
#
#
# print(StaticClass.print_same_start())
#
# b = StaticClass()
# print(b.print_same_start())

# class SameClass():
#     @staticmethod
#     def print_same_text():
#         print("I'm onli func, I cant use clas menthod and atribut")
#
#
# class SameClasseMethod():
#     a = 10
#
#     @classmethod
#     def minus_int_same(cls):
#         cls.a -= 1
#         return cls.a
#
#
# bob = SameClasseMethod()
# print(bob.minus_int_same())
# print(SameClasseMethod.minus_int_same())
# sandy = SameClasseMethod()
# print(sandy.minus_int_same())

# class Lion:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'The object Lion - {self.name}'
#
#
#     def __str__(self):
#         return self.name
#
# class UserInside():
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __len__(self):
#         return len(self.name+self.surname)
#
# class Otrezok:
#     def __init__(self, start, finish):
#         self.start = start
#         self.finish = finish
#
#     def __len__(self):
#         return abs(self)
#
#     def __abs__(self):
#         return abs(self.finish - self.start)
#
#
# class Vector:
#
#     def __init__(self, *args):
#         print(args)
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    @property
    def area(self):
        return 0.5 * self.a * self.b

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area







