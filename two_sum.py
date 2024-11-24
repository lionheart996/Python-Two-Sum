# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
class Solution:
    def twoSum(self, list_of_numbers, target):
        for i in range(len(list_of_numbers) - 1):
            if int(list_of_numbers[i]) + int(list_of_numbers[i + 1]) == int(target):
                return [i, i + 1]
        return None


