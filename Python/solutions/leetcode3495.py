# 3495. Minimum Operations to Make Array Elements Zero
from math import ceil
from typing import List

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # O(n)
        # def total(n : int):
        #     t = 0
        #     for num in range(1, n + 1):
        #         t += ceil((num.bit_length()) / 2)
        #
        #     return t

        # O(log(n))
        def total(n: int) -> int:
            if n == 0:
                return 0

            length = n.bit_length()
            t = 0

            for l in range(1, length):
                count = 1 << (l - 1)
                t += count * ceil(l / 2)

            start = 1 << (length - 1)
            count = n - start + 1
            t += count * ceil(length / 2)

            return t

        operations = 0
        for l, r in queries:
            t = total(r) - total(l - 1)
            operations += ceil(t/2)
        return operations

if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations(queries = [[1,2],[2,4]]))  # 3
    print(sol.minOperations(queries = [[2,6]]))  # 4
