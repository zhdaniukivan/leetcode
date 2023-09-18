# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coord(self):
#         return self.x, self.y
#
# v = Vector(1, 2)
# res = v.get_coord()
# print(res)
#
# v2 = Vector(2, 1)
# res_2 = Vector.get_coord(v2)
# print(res_2)
# import copy
#
# list_1 = [1, 2, 3]
# # print(list_1 is copy.copy(list_1))
# print(list_1[1] is copy.copy(list_1)[1])
#
# def some_func(some_arg:list =[]):
#     some_arg.append(1)
#     return some_arg
#
# print(some_func())
# print(some_func())
# print(some_func())
# print(some_func())
#
# double = lambda x: x*x
# print(double(4))
#
# some_true = True
# resaslt = 1 if some_true else 0
# print(resaslt)

# time decorator
from datetime import datetime
#
# def time_decorator(func):
#     def new_func(*args, **kwargs):
#         print(f'start_decorator {datetime.now()}')
#         func(*args, **kwargs)
#         print(f'(finished decorator{datetime.now()}')
#     return new_func
#
#
# @time_decorator
# def count_number(x):
#     print([i for i in range(0, x+1)])
#
# b = count_number(100)
#
#
#


#
# from datetime import datetime
#
# def check_time(func):
#     def start_decorator(*args, **kwargs):
#         a = datetime.now()
#         func(*args, **kwargs)
#         print(f'time: {datetime.now()-a}')
#     return start_decorator
#
# @check_time
# def make_list(long):
#     print([i for i in range(0, long)])
#
# start = make_list(10000)

# def division(a: int, b: int) -> int:
#     return a/b
#
# try:
#     division(10, )
# except ZeroDivisionError:
#     print('we can not make division to 0')
# except TypeError:
#     print('we not found b')
# finally:
#     print('finish')


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validat(cls, args):
        return cls.MIN_COORD <= args <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        print(self.x, self.y)

vector = Vector(1, 2)
res = Vector.get_coord(vector)

vector_2 = Vector(-1, 2)
res_2 =vector_2.get_coord()

print(res, res_2)