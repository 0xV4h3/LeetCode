# 1. Two Sum
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}

        for i, num in enumerate(nums):
            if target - num in num_idx:
                return [i, num_idx[target - num]]
            num_idx[num] = i

        return []

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum(nums = [2,7,11,15], target = 9)) # [0,1]
    print(sol.twoSum(nums = [3,2,4], target = 6)) # [1,2]
    print(sol.twoSum(nums = [3,3], target = 6)) # [0,1]