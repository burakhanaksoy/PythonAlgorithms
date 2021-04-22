class Solution(object):
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    subs = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    def romanToInt(self, s):
        if len(s) < 1 or len(s) > 15:
            return 0
        elif s in Solution.subs.keys():
            return Solution.subs[s]
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
                result = 0
                for i in s:
                    result += Solution.numbers[i]
                for k, v in Solution.subs.items():
                    count = s.count(k)

                    result = result - count * v
            return result

            # 'LVIII'
# numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
solution = Solution()
print(solution.romanToInt("MCMXCIV"))
