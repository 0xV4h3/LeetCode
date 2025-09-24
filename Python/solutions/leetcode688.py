# 688. Knight Probability in Chessboard

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        probabilities = []
        for move in range(k + 1):
            probabilities.append([])
            for r in range(n):
                probabilities[move].append([0] * n)
        probabilities[0][row][column] = 1

        for move in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for direction in directions:
                        previous_i, previous_j = i - direction[0], j - direction[1]
                        if 0 <= previous_i < n and 0 <= previous_j < n:
                            probabilities[move][i][j] += probabilities[move - 1][previous_i][previous_j]

                    probabilities[move][i][j] /= 8

        total_probability = 0
        for i in range(n):
            for j in range(n):
                total_probability += probabilities[k][i][j]

        return total_probability

if __name__ == "__main__":
    sol = Solution()
    print(sol.knightProbability(n = 3, k = 2, row = 0, column = 0))
    print(sol.knightProbability(n = 1, k = 0, row = 0, column = 0))
    print(sol.knightProbability(n=3, k=1, row=1, column=1))