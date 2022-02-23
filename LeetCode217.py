"""
LeetCode #217 - Contains Duplicate

Solution in Python

Maksim Vakulenko - 2/23/22

"""

class Solution(object):
    def containsDuplicate(self, nums):
        if type(nums) != list:
            return "Not a list"
        elif len(nums) == len(set(nums)):
            return False
        else:
            return True

nums=[1,2,3,4,4]

number = Solution()
print("Are there duplicates? ")
print(number.containsDuplicate(nums))