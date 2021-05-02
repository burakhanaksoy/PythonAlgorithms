class Solution(object):
    def removeDuplicates(self, nums):
        my_set = set(nums)
        my_list = list(my_set)
        print(f'{len(my_list)}, nums= {my_list}')

obj = Solution()
obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4])