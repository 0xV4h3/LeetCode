# 3459. Length of Longest V-Shaped Diagonal Segment
from functools import lru_cache
from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        dirs = ((-1, 1), (1, 1), (1, -1), (-1, -1))
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(i: int, j: int, turned: bool, num: int, d: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != num:
                return 0
            next_num = 0 if num == 2 else 2
            dx, dy = dirs[d]
            res = 1 + dfs(i + dx, j + dy, turned, next_num, d)
            if not turned:
                nd = (d + 1) % 4
                ndx, ndy = dirs[nd]
                res = max(res, 1 + dfs(i + ndx, j + ndy, True, next_num, nd))
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for d in range(4):
                        ans = max(ans, dfs(i, j, False, 1, d))
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.lenOfVDiagonal(grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]])) # 5
    print(sol.lenOfVDiagonal(grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]])) # 4
    print(sol.lenOfVDiagonal(grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]])) # 5
    print(sol.lenOfVDiagonal(grid = [[1]])) # 1
