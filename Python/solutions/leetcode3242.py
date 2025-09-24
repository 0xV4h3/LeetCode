# 3242. Design Neighbor Sum Service
from typing import List

class NeighborSum:
    adjacent_neighbors = ((0, -1), (-1, 0), (0, 1), (1, 0))
    diagonal_neighbors = ((-1, -1), (-1, 1), (1, 1), (1, -1))

    def __init__(self, grid: List[List[int]]):
        self.n = len(grid)
        self.grid = grid
        self.value_dict = {val: (i, j) for i, row in enumerate(grid) for j, val in enumerate(row)}

    def adjacentSum(self, value: int) -> int:
        adj_sum = 0
        val_coords = self.value_dict[value]
        for di, dj in NeighborSum.adjacent_neighbors:
            i = val_coords[0] + di
            j = val_coords[1] + dj
            if 0 <= i < self.n and 0 <= j < self.n:
                adj_sum += self.grid[i][j]

        return adj_sum

    def diagonalSum(self, value: int) -> int:
        diag_sum = 0
        val_coords = self.value_dict[value]
        for di, dj in NeighborSum.diagonal_neighbors:
            i = val_coords[0] + di
            j = val_coords[1] + dj
            if 0 <= i < self.n and 0 <= j < self.n:
                diag_sum += self.grid[i][j]

        return diag_sum

if __name__ == "__main__":
    neighbor1 = NeighborSum([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    print(neighbor1.adjacentSum(1)) # 6
    print(neighbor1.adjacentSum(4)) # 16
    print(neighbor1.diagonalSum(4)) # 16
    print(neighbor1.diagonalSum(8)) # 4

    neighbor2 = NeighborSum([[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]])
    print(neighbor2.adjacentSum(15)) #23
    print(neighbor2.diagonalSum(9)) # 45
