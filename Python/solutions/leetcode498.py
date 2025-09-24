# 498. Diagonal Traverse
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal = []
        m = len(mat)
        n = len(mat[0])
        i = 0
        j = 0
        k = 0
        isUp = True


        while k < m * n:
            if isUp:
                while i >= 0 and j < n:
                    diagonal.append(mat[i][j])
                    k += 1
                    j += 1
                    i -= 1

                if i < 0 and j <= n - 1:
                    i = 0
                if j == n:
                    i = i + 2
                    j -= 1

            else:
                while j >= 0 and i < m:
                    diagonal.append(mat[i][j])
                    k += 1
                    i += 1
                    j -= 1

                if j < 0 and i <= m - 1:
                    j = 0
                if i == m:
                    j = j + 2
                    i -= 1

            isUp = not isUp

        return diagonal

if __name__ == "__main__":
    sol = Solution()
    print(sol.findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]])) # [1,2,4,7,5,3,6,8,9]
    print(sol.findDiagonalOrder(mat = [[1,2],[3,4]])) # [1,2,3,4]