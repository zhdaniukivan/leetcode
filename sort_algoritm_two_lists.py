#
# Напишите программу, которая находит в массиве элемент, самый близкий по величине к данному числу.
#
# В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива. Во второй строке содержатся
# N чисел – элементы массива (целые числа, не превосходящие по модулю 1000). В третьей строке вводится одно целое число
# x, не превосходящее по модулю 1000.
# Формат вывода
#
# Вывести значение элемента массива, ближайшее к x. Если таких чисел несколько, выведите любое из них.
# Ограничения
#
# Ограничение времени
#
#     1 с
#
# Ограничение памяти


# size_of_list = int(input())
# some_list = [int(value) for value in input().split()]
# some_int = int(input())

size_of_list = 5
some_list = [1, 2, 3, 4, 5]
# some_list = [5, 4, 3, 2, 1]
some_int = 6
def return_the_moust_close_int(some_list: list, some_int: int) -> int:
    nearest_int = some_list[0]

    for i in some_list:
        if i / some_int == 1:
            return i
        elif i / some_int < i / nearest_int and i // some_int < i // nearest_int:
            nearest_int = i
    return nearest_int

print(return_the_moust_close_int(some_list, some_int))