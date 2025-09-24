# 2348. Number of Zero-Filled Subarrays
from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count, streak = 0, 0

        for num in nums:
            if num != 0:
                streak = 0
            else:
                streak += 1
                count += streak

        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.zeroFilledSubarray(nums = [1,3,0,0,2,0,0,4])) # 6
    print(sol.zeroFilledSubarray(nums = [0,0,0,2,0,0]))  # 9
    print(sol.zeroFilledSubarray(nums = [2, 10, 2019]))  # 0
