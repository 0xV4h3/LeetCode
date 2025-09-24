# 54. Spiral Matrix
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_order = []
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                spiral_order.append(matrix[top][col])
            top += 1

            for row in range(top, bottom + 1):
                spiral_order.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    spiral_order.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    spiral_order.append(matrix[row][left])
                left += 1

        return spiral_order

if __name__ == "__main__":
    sol = Solution()
    print(sol.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))  # [1,2,3,6,9,8,7,4,5]
    print(sol.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))  # [1,2,3,4,8,12,11,10,9,5,6,7]