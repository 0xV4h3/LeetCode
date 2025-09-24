# 2664. The Knight’s Tour
from typing import List
import time

class Solution:
    def __init__(self):
        self.directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    def tourOfKnight(self, m: int, n: int, start_row: int, start_col: int) -> List[List[int]]:
        def backtrack(row: int, col: int) -> bool:
            if grid[row][col] == (m * n) - 1:
                return True

            for d_row, d_col in self.directions:
                next_row, next_col = row + d_row, col + d_col
                if 0 <= next_row < m and 0 <= next_col < n:
                    if grid[next_row][next_col] == -1:
                        grid[next_row][next_col] = grid[row][col] + 1
                        if backtrack(next_row, next_col):
                            return True
                        grid[next_row][next_col] = -1

            return False

        grid = []
        for _ in range(m):
            grid.append([-1] * n)
        grid[start_row][start_col] = 0

        return grid if backtrack(start_row, start_col) else []

    def tourOfKnightWarnsdorffRule(self, m: int, n: int, start_row: int, start_col: int) -> List[List[int]]:
        def get_sorted_moves(row: int, col: int) -> List[tuple[int, int]]:
            moves = []
            for d_row, d_col in self.directions:
                next_row, next_col = row + d_row, col + d_col
                if 0 <= next_row < m and 0 <= next_col < n and grid[next_row][next_col] == -1:
                    degree = 0
                    for d2_row, d2_col in self.directions:
                        row2, col2 = next_row + d2_row, next_col + d2_col
                        if 0 <= row2 < m and 0 <= col2 < n and grid[row2][col2] == -1:
                            degree += 1
                    moves.append(((next_row, next_col), degree))
            moves.sort(key=lambda x: x[1])
            return [pos for pos, _ in moves]

        def backtrack(row: int, col: int) -> bool:
            if grid[row][col] == (m * n) - 1:
                return True

            for next_row, next_col in get_sorted_moves(row, col):
                grid[next_row][next_col] = grid[row][col] + 1
                if backtrack(next_row, next_col):
                    return True
                grid[next_row][next_col] = -1

            return False

        grid = []
        for _ in range(m):
            grid.append([-1] * n)
        grid[start_row][start_col] = 0

        return grid if backtrack(start_row, start_col) else []

    def checkValidGrid(self, grid: List[List[int]], start_row: int, start_col: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        position = (start_row, start_col)

        for move in range((m * n) - 1):
            valid = False
            for d_row, d_col in self.directions:
                next_row, next_col = position[0] + d_row, position[1] + d_col
                if 0 <= next_row < m and 0 <= next_col < n:
                    if grid[next_row][next_col] == grid[position[0]][position[1]] + 1:
                        position = (next_row, next_col)
                        valid = True
                        break

            if not valid:
                return False

        return True

if __name__ == "__main__":
    sol = Solution()
    minimum = 5
    m = int(input("Enter m: "))
    while m < 5:
        print(f"Knight's tour problem has no solution if m or n is smaller than {minimum}")
        m = int(input("Enter m: "))

    n = int(input("Enter n: "))
    while n < 5:
        print(f"Knight's tour problem has no solution if m or n is smaller than {minimum}")
        n = int(input("Enter n: "))

    row = int(input(f"Enter row(0-{m - 1}): "))
    while row > m - 1:
        print(f"Row should be in range 0 - {m - 1}")
        row = int(input("Enter row: "))

    col = int(input(f"Enter column(0-{n - 1}): "))
    while col > n - 1:
        print(f"Column should be in range 0 - {n - 1}")
        col = int(input("Enter column: "))

    print("Choose knight's tour algorithm:")
    print("1 - Backtracking (slow)")
    print("2 - Warnsdorff's heuristic (fast)")
    algo_choice = input("Enter your choice (1 or 2): ")

    while algo_choice not in ("1", "2"):
        algo_choice = input("Please enter 1 or 2: ")
    use_warnsdorff = algo_choice == "2"

    start = time.time()
    grid = sol.tourOfKnightWarnsdorffRule(m, n, row, col) if use_warnsdorff else sol.tourOfKnight(m, n, row, col)
    end = time.time()

    nums = [c for r in grid for c in r]
    if len(set(nums)) == m * n and sol.checkValidGrid(grid, row, col):
        print("Knight's tour problem solved!!!")
    else:
        print("Something goes wrong:(")

    max_step = m * n - 1
    cell_width = len(str(max_step))

    print("┌" + ("─" * (cell_width + 1) + "┬") * (n - 1) + "─" * (cell_width + 1) + "┐")

    for i, row in enumerate(grid):
        print("│" + "│".join(str(col).rjust(cell_width + 1) for col in row) + "│")

        if i < m - 1:
            print("├" + ("─" * (cell_width + 1) + "┼") * (n - 1) + "─" * (cell_width + 1) + "┤")

    print("└" + ("─" * (cell_width + 1) + "┴") * (n - 1) + "─" * (cell_width + 1) + "┘")
    print(f"Completed in {end - start:.2f} seconds")


