class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                nums.pop(i-1)
                i+=1
            else:
                i-=1
        return len(nums)

solution = Solution()

print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
