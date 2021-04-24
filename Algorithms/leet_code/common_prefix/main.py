# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight",'araba']
# Output: "fl"

class Solution(object):
    def longestCommonPrefix(self, strs):
        key = strs[0]
        count = len(key)
        for s in strs[1:]:
            count = len(s) if len(s) < count else count
            for i in range(count, -1, -1):
                if s[:i] == key[:i]:
                    count = i
                    break
        return key[:count]
