# 1792. Maximum Average Pass Ratio
import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def calculateGain(p: int, t: int) -> float:
            return (p + 1) / (t + 1) - p / t

        max_heap = []
        for p, t in classes:
            gain = calculateGain(p, t)
            heapq.heappush(max_heap, (-gain, p, t))

        for _ in range(extraStudents):
            current_gain, p, t = heapq.heappop(max_heap)
            p += 1
            t += 1
            new_gain = calculateGain(p, t)
            heapq.heappush(max_heap, (-new_gain, p, t))

        total_pass_ratio = sum(p / t for _, p, t in max_heap)
        return total_pass_ratio / len(classes)

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2))  # 0.78333
    print(sol.maxAverageRatio(classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4))  # 0.53485