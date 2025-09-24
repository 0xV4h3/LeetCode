# 1504. Count Submatrices With All Ones
from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0

        heights = [0] * len(mat[0])
        submatrices  = 0

        for row in mat:
            for i, x in enumerate(row):
                heights[i] = 0 if x == 0 else heights[i] + 1
            stack = [[-1, 0, -1]]
            for i, h in enumerate(heights):
                while stack[-1][2] >= h:
                    stack.pop()
                j, prev, _ = stack[-1]
                cur = prev + (i - j) * h
                stack.append([i, cur, h])
                submatrices += cur

        return submatrices

if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubmat(mat = [[1,0,1],[1,1,0],[1,1,0]])) # 13
    print(sol.numSubmat(mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]))  # 24