# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

array = [3, 3]
tar = 6


class Solution(object):
    def twoSum(self, nums, target):
        index1, index2 = 0, 0
        for i in range(len(nums)):
            index1 = i
            checked = target - nums[i]
            try:
                index2 = nums.index(checked)
                if index2 != index1:
                    return [index1, index2]
            except ValueError:
                pass
        return []


obj = Solution()
print(obj.twoSum(array, tar))
