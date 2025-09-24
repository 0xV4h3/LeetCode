# 41. First Missing Positive
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if 1 <= num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.firstMissingPositive(nums = [1,2,0]))  # 3
    print(sol.firstMissingPositive(nums = [3,4,-1,1]))  # 2
    print(sol.firstMissingPositive(nums = [7,8,9,11,12]))  # 1