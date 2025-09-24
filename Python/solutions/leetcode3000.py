# 3000. Maximum Area of Longest Diagonal Rectangle
from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        max_diagonal = 0
        for l, w in dimensions:
            diagonal = l * l + w * w
            if diagonal > max_diagonal:
                max_diagonal = diagonal
                max_area = l * w
            elif diagonal == max_diagonal:
                max_area = max(max_area, l * w)
        return max_area

if __name__ == "__main__":
    sol = Solution()
    print(sol.areaOfMaxDiagonal(dimensions = [[9,3],[8,6]])) # 48
    print(sol.areaOfMaxDiagonal(dimensions = [[3,4],[4,3]])) # 12