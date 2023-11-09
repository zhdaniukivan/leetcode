from functools import wraps

def same_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('start decorator')
        res = func(*args, **kwargs)
        print(res)
        print('print stop')
        return res
    return wrapper

@same_decorator
def same_func(a, b, c: int) -> int:
    return a+b+c


same_func(1, 2, 3)


class SameClass:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'I now thet integer :{self.a}, {self.b}, {self.c}'

bob = SameClass(1, 2, 3)
print(bob)











