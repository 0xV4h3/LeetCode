# 1317. Convert Integer to the Sum of Two No-Zero Integers
from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n):
            b = n - a
            if '0' not in str(a) and '0' not in str(b):
                return [a, b]

        return []

if __name__ == "__main__":
    sol = Solution()
    print(sol.getNoZeroIntegers(n = 2))  # [1,1]
    print(sol.getNoZeroIntegers(n = 11))  # [2,9]