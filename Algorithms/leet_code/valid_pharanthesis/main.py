class Solution(object):
    def isValid(self, s):
        my_list = []
        opens = ['{', '(', '[']
        closers = {'{': '}', '(': ')', '[': ']'}
        for char in s:
            is_empty = False
            if len(my_list)==0 and char not in opens:
                return False
            if char in opens:
                my_list.append(char)
            elif closers[my_list.pop()] == char:
                is_empty = True
            else:
                return False

        return is_empty and len(my_list) == 0


object_solution = Solution()
# print()
s = "({{{{}}}))"
print(object_solution.isValid(s))
