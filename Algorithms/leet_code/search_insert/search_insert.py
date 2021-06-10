class Solution:
    def searchInsert(self, nums, target):
        temp = 0
        for i in range(len(nums)):
            if target > nums[i]:
                temp += 1
            elif target == nums[i]:
                return i
        return temp

solution = Solution()
print(solution.searchInsert([1], 0))
