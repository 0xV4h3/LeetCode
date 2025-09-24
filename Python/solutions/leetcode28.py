# 28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr(haystack = "sadbutsad", needle = "sad"))  # 0
    print(sol.strStr(haystack = "leetcode", needle = "leeto"))  # -1