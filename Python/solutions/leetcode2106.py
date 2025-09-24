# 2561. Rearranging Fruits
from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        if not fruits:
            return 0

        start = max(fruits[0][0], startPos - k)
        end = min(fruits[-1][0], startPos + k)
        size = end - start + 1
        offset = -start

        amount = [0] * size
        for pos, cnt in fruits:
            if start <= pos <= end:
                amount[pos + offset] = cnt

        prefix = [0] * (size + 1)
        for i in range(size):
            prefix[i + 1] = prefix[i] + amount[i]

        def interval_sum(lpos: int, rpos: int) -> int:
            lp = max(start, lpos)
            rp = min(end, rpos)
            if lp > rp:
                return 0
            return prefix[rp - start + 1] - prefix[lp - start]

        ans = 0

        maxR = min(end - startPos, k)
        for r in range(0, maxR + 1):
            l = max(0, k - 2 * r)
            ans = max(ans, interval_sum(startPos - l, startPos + r))

        maxL = min(startPos - start, k)
        for l in range(0, maxL + 1):
            r = max(0, k - 2 * l)
            ans = max(ans, interval_sum(startPos - l, startPos + r))

        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxTotalFruits([[2,8],[6,3],[8,6]], startPos=5, k=4))
    print(sol.maxTotalFruits([[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos=5, k=4))
    print(sol.maxTotalFruits([[0,3],[6,4],[8,5]], startPos=3, k=2))
    print(sol.maxTotalFruits([[20000, 10000]], startPos=20000, k=0))
