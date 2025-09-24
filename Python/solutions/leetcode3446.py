# 3446. Sort Matrix by Diagonals
from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diag_map = {i: [] for i in range(-(n - 1), n)}
        for i in range(n):
            for j in range(n):
                diag_map[i - j].append(grid[i][j])

        for d in diag_map:
            if d >= 0:
                diag_map[d].sort()
            else:
                diag_map[d].sort(reverse=True)

        for i in range(n):
            for j in range(n):
                grid[i][j] = diag_map[i - j].pop()

        return grid

if __name__ == "__main__":
    sol = Solution()
    print(sol.sortMatrix(grid = [[1,7,3],[9,8,2],[4,5,6]]))  # [[8,2,3],[9,6,7],[4,5,1]]
    print(sol.sortMatrix(grid = [[0,1],[1,2]]))  # [[2,1],[1,0]]
    print(sol.sortMatrix(grid = [[1]])) # [[1]]