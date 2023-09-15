class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y

v = Vector(1, 2)
res = v.get_coord()
print(res)

v2 = Vector(2, 1)
res_2 = Vector.get_coord(v2)
print(res_2)
import copy

list_1 = [1, 2, 3]
# print(list_1 is copy.copy(list_1))
print(list_1[1] is copy.copy(list_1)[1])

def some_func(some_arg:list =[]):
    some_arg.append(1)
    return some_arg

print(some_func())
print(some_func())
print(some_func())
print(some_func())

double = lambda x: x*x
print(double(4))

some_true = True
resaslt = 1 if some_true else 0
print(resaslt)


