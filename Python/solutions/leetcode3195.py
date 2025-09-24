# 3195. Find the Minimum Area to Cover All Ones I
from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_row, max_row = m, -1
        min_col, max_col = n, -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)

        return (max_row - min_row + 1) * (max_col - min_col + 1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumArea(grid = [[0,1,0],[1,0,1]])) # 6
    print(sol.minimumArea(grid = [[1,0],[0,0]]))  # 1