class Solution(object):
    def isPalindrome(self, x):
        my_list = [num for num in str(x)]
        if my_list[0] == '-':
            return False
        if my_list[::] == my_list[::-1]:
            return True
        return False
        
        # 54245
        # 4224

obj = Solution()
print(obj.isPalindrome(1211))
