from functools import wraps


def same_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("start")
        res = func(*args, **kwargs)
        print("stop")
        return res
    return wrapper


@same_decorator
def print_my_name(name: str) -> str:
    print(name)
    return name

print_my_name("Ivan")


def same_func(i):
    if i % 2 == 0:
        return 48
    else:
        return 56


b = {i: same_func(i) for i in range(11)}
print(b)

print(10%2)


print('------------')
def same_func(same_text):
    if isinstance(same_text, str):
        return same_text
    else:
        x = 10 if len(b) > 10 else 20
        return x


print(same_func(1))


class SameClass:

    def __init__(self, same_int):
        self.same_int = same_int

    def chet_ne_chet(self):
        if self.same_int % 2 == 0:
            return 'chet'
        else:
            return 'ne chet'


bob = SameClass(12)
print(bob.chet_ne_chet())

b = 'sandy'
b.
