"""
LeetCode #9 - Palindrome Number

Solution in Python

Maksim Vakulenko - 2/14/22

"""


class Solution(object):
    def isPalindrone(self, x):
        if x < 0:
            return "Negative number can't be a Palindrone"
        elif type(x) != int:
            return "Input is not an integer"
        else:
            z = [int(a) for a in str(x)]
            print(z)
            y = list(reversed(z))
            print(y)
            if z == y:
                bool = True
            else:
                bool = False
            return bool


number = Solution()
print(number.isPalindrone(100222221))