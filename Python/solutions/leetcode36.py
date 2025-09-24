# 36. Valid Sudoku
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        def box_id(i: int, j: int) -> int:
            return (i // 3) * 3 + (j // 3)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                b = box_id(i, j)
                if num in rows[i] or num in cols[j] or num in boxes[b]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[b].add(num)
        return True

    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     numbers = {str(i): {'box' : {}, 'row' : {}, 'column' : {} } for i in range(1, 10)}
    #
    #     def box_id(i : int, j : int) -> int:
    #         return (i // 3) * 3 + (j // 3)
    #
    #     for i in range(9):
    #         for j in range(9):
    #             if board[i][j] == '.': continue
    #             num = board[i][j]
    #             num_box = box_id(i, j)
    #             if  num_box in numbers[num]['box']:
    #                 return False
    #             else:
    #                 numbers[num]['box'][num_box] = 1
    #
    #             if i in  numbers[num]['row']:
    #                 return False
    #             else:
    #                 numbers[num]['row'][i] = 1
    #
    #             if j in numbers[num]['column']:
    #                 return False
    #             else:
    #                 numbers[num]['column'][j] = 1
    #
    #     return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValidSudoku(board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])) # True
    print(sol.isValidSudoku(board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])) # False