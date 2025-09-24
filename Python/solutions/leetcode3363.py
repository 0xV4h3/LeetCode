# 3363. Find the Maximum Number of Fruits Collected
from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        sum_diagonal = sum(fruits[i][i] for i in range(n))
        sum_second_third = 0

        for turn in range(2):
            if turn == 1:
                for i in range(n):
                    for j in range(i+1, n):
                        fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]

            dp = [[-1] * n for _ in range(n)]
            dp[0][n - 1] = fruits[0][n - 1]

            for i in range(1, n - 1):
                for j in range(n):
                    for dj in (-1, 0, 1):
                        prev_j = j + dj
                        if 0 <= prev_j < n and dp[i - 1][prev_j] != -1:
                            dp[i][j] = max(dp[i][j], dp[i - 1][prev_j] + fruits[i][j])

            sum_second_third += dp[n - 2][n - 1]

        return sum_diagonal + sum_second_third

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxCollectedFruits(fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]])) # 100
    print(sol.maxCollectedFruits(fruits = [[1,1],[1,1]])) # 4
    print(sol.maxCollectedFruits([[8,5,0,17,15],[6,0,15,6,0],[7,19,16,8,18],[11,3,2,12,13],[17,15,15,4,6]])) #145
