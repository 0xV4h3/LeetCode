# 3025. Find the Number of Ways to Place People I
from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        pairs = 0
        n = len(points)

        for i in range(n):
            a = points[i]
            for j in range(n):
                b = points[j]
                if i == j or not (a[0] <= b[0] and a[1] >= b[1]):
                    continue

                if n == 2:
                    pairs += 1
                    continue

                contained = False
                for k in range(n):
                    if k == i or k == j:
                        continue

                    c = points[k]
                    if (a[0] <= c[0] <= b[0]) and (a[1] >= c[1] >= b[1]):
                        contained = True
                        break

                if not contained:
                    pairs += 1

        return pairs


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfPairs(points = [[1,1],[2,2],[3,3]]))  # 0
    print(sol.numberOfPairs(points = [[6,2],[4,4],[2,6]]))  # 2
    print(sol.numberOfPairs(points = [[3,1],[1,3],[1,1]]))  # 2
