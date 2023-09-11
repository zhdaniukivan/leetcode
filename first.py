# class Point:
#     'class dlay opredeleniya coordinat'
#     color = 'red'
#     circle = 2
#
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
#
#     def __del__(self):
#         print('delete pt' + str(self))
#
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return (self.x, self.y)
#
#
# pt = Point()
# # pt.set_coords(1, 2)
# print(pt.__dict__)

# class Point:
#     def __new__(cls, *args, **kwargs):
#         print('start method __new__ for ' + str(cls))
#         return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print('start method __init__ for ' + str(self))
#         self.x = x
#         self.y = y
#
# pt = Point(1, 2)
# print(pt)


# class DataBase:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance=super().__new__(cls)
#         return cls.__instance
#
#     def __del__(self):
#         DataBase.__instance = None
#
#     def __init__(self, user, password, port):
#         self.user = user
#         self.password = password
#         self.port = port
#
#     def connect(self):
#         print(f'connected to bd')
#
#     def close(self):
#         print(f'close connection')
#
# db = DataBase('root', '1234', '3342')
# db2 = DataBase('root2', '111', '3342')
#
# print(id(db)==id(db2))
# strs = ["fltrower","fltrow","flright"]
# count = 0
# answer_str =''
# last_word = len(strs)-2
# print(last_word)
# count_number_of_words = 0
# word = 0
# string = 0
# a = True
# while a == True:
#     if strs[word][string]==strs[word+1][string] and word != last_word:
#         word =+1
#         print('1')
#     elif strs[word][string]==strs[word+1][string] and word == last_word:
#         answer_str +=strs[word][string]
#         word = 0
#         string += 1
#         print('2')
#     elif strs[word][string]!=strs[word+1][string]:
#         print(answer_str)
#         break

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        self.strs = strs

        answer_str = ''
        last_word = len(strs) - 2

        word = 0
        string = 0
        a = True
        min_str = 200
        for i in self.strs:
            if len(i) < min_str:
                min_str = len(i)
        if min_str == 0:
            return ''

        if self.strs == [""]:
            return ''
        if len(self.strs) == 1:
            return str(self.strs[0])
        else:
            while a == True:
                if strs[word][string] == strs[word + 1][string] and word != last_word:
                    word = +1
                elif strs[word][string] == strs[word + 1][string] and word == last_word:
                    if min_str == string + 1:
                        answer_str += strs[word][string]
                        return answer_str

                    elif min_str > string + 1:
                        answer_str += strs[word][string]
                        word = 0
                        string += 1
                    else:
                        return answer_str
                elif strs[word][string] != strs[word + 1][string]:
                    return answer_str
                    break


start = Solution()
print(start.longestCommonPrefix(["flower","flower","flower","flower"]))
