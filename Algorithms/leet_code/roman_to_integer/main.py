class Solution(object):
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    subs = {'IV': 2, 'IX': 2, 'XL': 20, 'XC': 20, 'CD': 200, 'CM': 200}

    def romanToInt(self, s):
        result = 0
        if len(s) < 1 or len(s) > 15:
            return 0
        else:
            key_error = False
            for c in s:
                try:
                    Solution.numbers[c]
                except KeyError:
                    key_error = True
            if key_error:
                return 0
            else:
                for i in s:
                    result += Solution.numbers[i]
                for k, v in Solution.subs.items():
                    count = s.count(k)
                    result = result - count * v
            return result

            # 'LVIII'
# numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
solution = Solution()
print(solution.romanToInt("IV"))
