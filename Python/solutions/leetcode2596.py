# 2596. Check Knight Tour Configuration
from typing import List

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        n = len(grid[0])
        position = (0, 0)

        for move in range((n * n) - 1):
            valid = False
            for d_row, d_col in directions:
                next_i, next_j = position[0] + d_row, position[1] + d_col
                if 0 <= next_i < n and 0 <= next_j < n:
                    if grid[next_i][next_j] == grid[position[0]][position[1]] + 1:
                        position = (next_i, next_j)
                        valid = True
                        break

            if not valid:
                return False

        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.checkValidGrid(grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]))
    print(sol.checkValidGrid(grid = [[0,3,6],[5,8,1],[2,7,4]]))
    print(sol.checkValidGrid(grid = [[8,3,6],[5,0,1],[2,7,4]]))