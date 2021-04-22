# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
# then return 0.

class Solution(object):
    def reverse(self, x):
        if x < -2**31 or x > 2**31 -1:
            return 0
        else:
            list = [num for num in str(x)]
            is_negative = False
            if list[0] == '-':
                is_negative = True
            if is_negative:
                reversed_list = list[len(list):0:-1]
            else:
                reversed_list = list[::-1]

            my_str = ''
            for i in reversed_list:
                my_str = my_str + i
            if is_negative:
                return int(my_str) * -1
            return int(my_str)


a = Solution()
print(a.reverse(-100))
