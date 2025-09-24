# 10. Regular Expression Matching
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.fullmatch(p, s))

if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch(s = "aa", p = "a")) # False
    print(sol.isMatch(s = "aa", p = "a*"))  # True
    print(sol.isMatch(s = "ab", p = ".*"))  # True