# 3027. Find the Number of Ways to Place People II
from math import inf
from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        pairs = 0
        points.sort(key=lambda p: (p[0], -p[1]))
        for i, (x1, y1) in enumerate(points):
            y = -inf
            for (x2, y2) in points[i + 1:]:
                if y1 >= y2 > y:
                    pairs += 1
                    y = y2
        return pairs

if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfPairs(points = [[1,1],[2,2],[3,3]]))  # 0
    print(sol.numberOfPairs(points = [[6,2],[4,4],[2,6]]))  # 2
    print(sol.numberOfPairs(points = [[3,1],[1,3],[1,1]]))  # 2