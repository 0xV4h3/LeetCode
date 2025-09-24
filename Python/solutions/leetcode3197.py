# 3197. Find the Minimum Area to Cover All Ones II
import sys
from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        rotated_grid = self.rotate_matrix_counterclockwise(grid)
        return min(self.sections(grid), self.sections(rotated_grid))

    def rotate_matrix_counterclockwise(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        ret = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                ret[m - j - 1][i] = grid[i][j]

        return ret

    def sections(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        res = n * m

        for i in range(n - 1):
            for j in range(m - 1):
                res = min(
                    res,
                    self.minimumArea(grid, 0, i, 0, m - 1)
                    + self.minimumArea(grid, i + 1, n - 1, 0, j)
                    + self.minimumArea(grid, i + 1, n - 1, j + 1, m - 1),
                )

                res = min(
                    res,
                    self.minimumArea(grid, 0, i, 0, j)
                    + self.minimumArea(grid, 0, i, j + 1, m - 1)
                    + self.minimumArea(grid, i + 1, n - 1, 0, m - 1),
                )

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                res = min(
                    res,
                    self.minimumArea(grid, 0, i, 0, m - 1)
                    + self.minimumArea(grid, i + 1, j, 0, m - 1)
                    + self.minimumArea(grid, j + 1, n - 1, 0, m - 1),
                )

        return res

    def minimumArea(self, grid: List[List[int]], u: int, d: int, l: int, r: int) -> int:
        min_row, max_row = len(grid), 0
        min_col, max_col = len(grid[0]), 0

        for i in range(u, d + 1):
            for j in range(l, r + 1):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    min_col = min(min_col, j)
                    max_row = max(max_row, i)
                    max_col = max(max_col, j)

        if min_row <= max_row:
            return (max_row - min_row + 1) * (max_col - min_col + 1)

        return sys.maxsize // 3

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumSum(grid = [[1,0,1],[1,1,1]])) # 5
    print(sol.minimumSum(grid = [[1,0,1,0],[0,1,0,1]]))  # 5