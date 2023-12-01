import collections


check_the_list = [1, 2, 3, 4, 5, 1, 2, 1]
result = collections.Counter(check_the_list)
print(result)
print(result[1])
print(result.most_common(2))


def check_list(same_list: list) -> dict:
    resalt_dict = {}
    for i in same_list:
        if i in resalt_dict:
            resalt_dict[i] += 1
        else:
            resalt_dict[i] = 1
    return resalt_dict

bob = check_list(check_the_list)
print(bob)

same_dict = collections.defaultdict(str)

same_dict['name']= 'bob'
same_dict['surname'] = 'Zhdaniuk'
same_dict['age']
print(same_dict)

title = ('name', 'age', 'surname')
User = collections.namedtuple('User', title)
user_1 = User('Ivan', 35, 'Zhdaniuk')
print(user_1)