# 118. Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            triangle = [[1], [1,1]]
            for row in range(2, numRows):
                triangle.append([1])
                for column in range(1, row):
                    triangle[row].append(triangle[row - 1][column - 1] + triangle[row - 1][column])
                triangle[row].append(1)
            return triangle

if __name__ == "__main__":
    sol = Solution()
    example1 = sol.generate(numRows = 5)
    print(example1)
    example2 = sol.generate(numRows = 1)
    print(example2)