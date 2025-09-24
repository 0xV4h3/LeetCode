# 14. Longest Common Prefix
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:len(prefix) - 1]
                if prefix == '':
                    return ''

        return prefix

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(strs = ["flower","flow","flight"])) # "fl"
    print(sol.longestCommonPrefix(strs = ["dog","racecar","car"]))  # ""