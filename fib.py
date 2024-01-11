def fac(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return fac(x-1) * x


bob = fac(4)
print(bob)