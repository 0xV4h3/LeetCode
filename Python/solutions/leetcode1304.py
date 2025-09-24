# 1304. Find N Unique Integers Sum up to Zero
from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [i for x in range(1, n // 2 + 1) for i in (x, -x)] + ([0] if n % 2 else [])

if __name__ == "__main__":
    sol = Solution()
    print(sol.sumZero(5))  # [1, -1, 2, -2, 0]
    print(sol.sumZero(3))  # [1, -1, 0]
    print(sol.sumZero(1))  # [0]
    print(sol.sumZero(4))  # [1, -1, 2, -2]