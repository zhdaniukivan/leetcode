class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a, b, c = 0, 0, 0

        for i in s:
            if i == "(" or i == ')':
                if i == '(':
                    a += 1
                if i == ')':
                    a -= 1
                    if a < 0:
                        return False
            if i == "{" or i == '}':
                if i == '{':
                    b += 1
                if i == '}':
                    b -= 1
                    if b < 0:
                        return False
            if i == "[" or i == ']':
                if i == '[':
                    c += 1
                if i == ']':
                    c -= 1
                    if c < 0:
                        return False
            else:
                return False
        if a == 0 and b == 0 and c == 0:
            return True
        else:
            return False

a = Solution()
b = a.isValid('()[]{}')
print(b)