# Given an array nums and a value val,
# remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.

class Solution:
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


solution = Solution()
print(solution.removeElement([0,1,2,2,3,0,4,2], 2))
