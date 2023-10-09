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

class Couter:
    current: int

    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        current = self.current
        self.current += 1
        return current

c = Couter()
i = iter(c)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

# for i in c:
#     print(i)


def some():
    yield 1

b = some()
print(next(b))


try:
    b = some()
    print(next(b))
    print(next(b))
except:
    print('1111')
finally:
    print('func is stopped')



    



