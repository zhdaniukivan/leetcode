import random

a = [random.randint(1, 10) for i in range(1, 10)]
print(a)


class SimpleSort:

    def __init__(self, same_list):
        self.same_list = same_list
        self.sorted_list = []

    def find_smallest(self, sub_list):
        print('start 1')
        smallest = sub_list[0]
        smallest_index = 0
        for i in range(0, len(sub_list)):
            if sub_list[i] < smallest:
                smallest = sub_list[i]
                smallest_index = i
                print(smallest, smallest_index)
        return smallest_index

    def simple_sort(self):
        print('start 2')
        for i in range(len(self.same_list)):
            smallest = self.find_smallest(self.same_list)
            self.sorted_list.append(self.same_list.pop(smallest))
        return self.sorted_list


bob = SimpleSort(a)
bob.simple_sort()
print(bob.sorted_list)
