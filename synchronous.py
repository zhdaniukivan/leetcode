import time


def func_1(x):
    print(x ** 2)
    time.sleep(3)
    print('func_1 finished')


def func_2(x):
    print(x * 0.5)
    time.sleep(3)
    print('func_2 finished')


def main():
    func_1(4)
    func_2(4)


print(time.strftime('%X'))

main()

print(time.strftime('%X'))
