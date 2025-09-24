# 45. Jump Game II
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n for _ in range(n)]
        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                dp[i] = min(dp[i], 1 + dp[min(n - 1, i + j)])

        return dp[0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.jump(nums = [2,3,1,1,4])) # 2
    print(sol.jump(nums = [2,3,0,1,4])) # 2