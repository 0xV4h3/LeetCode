class Solution:
    def dfs(self, grid, r, c):
        row = len(grid)
        col = len(grid[0])
        row_neighbours = [-1, 0, 0, 1]
        col_neighbours = [0, -1, 1, 0]
        grid[r][c] = '0'
        for i in range(4):
            new_row = r + row_neighbours[i]
            new_column = c + col_neighbours[i]
            if (0 <= new_row < row) and (0 <= new_column < col) and grid[new_row][new_column] == '1':
                self.dfs(grid, new_row, new_column)

    def numIslands(self, grid: list[list[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        number_of_islands = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    number_of_islands += 1
        return number_of_islands

if __name__ == "__main__":
    sol = Solution()
    grid1 = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    print(f"Grid: {grid1}")
    print(f"Output: {sol.numIslands(grid1)}")

    grid2 = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    print(f"Grid: {grid1}")
    print(f"Output: {sol.numIslands(grid2)}")



