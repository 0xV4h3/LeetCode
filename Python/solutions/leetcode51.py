# 51. N-Queens
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(r : int):
            if r == n:
                sol = []
                for i in range(n):
                    row = ['.'] * n
                    row[board[i]] = 'Q'
                    sol.append("".join(row))
                solutions.append(sol)
                return

            for c in range(n):
                if cols[c] or d1[r + c] or d2[r - c + n - 1]:
                    continue
                board[r] = c
                cols[c] = d1[r + c] = d2[r - c + n - 1] = True

                backtrack(r + 1)

                cols[c] = d1[r + c] = d2[r - c + n - 1] = False

        solutions = []
        board = [0] * n

        cols = [False] * n
        d1 = [False] * (2 * n - 1)
        d2 = [False] * (2 * n - 1)

        backtrack(0)
        return solutions

if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(n = 4))
    print(sol.solveNQueens(n = 1))