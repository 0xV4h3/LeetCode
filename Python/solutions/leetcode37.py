# 37. Sudoku Solver
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> List[List[str]]:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        def box_id(i: int, j: int) -> int:
            return (i // 3) * 3 + (j // 3)

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == '.':
                    empty.append((row, col))
                else:
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_id(row, col)].add(num)

        def backtrack(k : int) -> bool:
            if k == len(empty):
                return True

            row, col = empty[k]
            box = box_id(row, col)

            for num in "123456789":
                if num not in rows[row] and num not in cols[col] and num not in boxes[box]:
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)
                    if backtrack(k + 1):
                        return True
                    board[row][col] = '.'
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box].remove(num)
            return False

        backtrack(0)
        return board

if __name__ == "__main__":
    sol = Solution()
    print(sol.solveSudoku(board =
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]))
# [["5", "3", "4", "6", "7", "8", "9", "1", "2"]
# ,["6", "7", "2", "1", "9", "5", "3", "4", "8"]
# ,["1", "9", "8", "3", "4", "2", "5", "6", "7"]
# ,["8", "5", "9", "7", "6", "1", "4", "2", "3"]
# ,["4", "2", "6", "8", "5", "3", "7", "9", "1"]
# ,["7", "1", "3", "9", "2", "4", "8", "5", "6"]
# ,["9", "6", "1", "5", "3", "7", "2", "8", "4"]
# ,["2", "8", "7", "4", "1", "9", "6", "3", "5"]
# ,["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

    grid = sol.solveSudoku(board =
    [[".",".",".",".",".",".",".",".","."]
    ,[".",".",".",".",".",".",".",".","."]
    , [".", ".", ".", ".", ".", ".", ".", ".", "."]
    , [".", ".", ".", ".", ".", ".", ".", ".", "."]
    , [".", ".", ".", ".", ".", ".", ".", ".", "."]
    , [".", ".", ".", ".", ".", ".", ".", ".", "."]
    , [".", ".", ".", ".", ".", ".", ".", ".", "."]
    , [".", ".", ".", ".", ".", ".", ".", ".", "."]
    , [".", ".", ".", ".", ".", ".", ".", ".", "."]])

    for line in grid:
        print(line)