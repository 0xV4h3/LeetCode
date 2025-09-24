# 1493. Longest Subarray of 1's After Deleting One Element
from typing import List

class Solution:
    # def longestSubarray(self, nums: List[int]) -> int:
    #     left = 0
    #     zero_count = 0
    #     max_len = 0
    #
    #     for right in range(len(nums)):
    #         if nums[right] == 0:
    #             zero_count += 1
    #
    #         while zero_count > 1:
    #             if nums[left] == 0:
    #                 zero_count -= 1
    #             left += 1
    #
    #         max_len = max(max_len, right - left + 1)
    #
    #     return max_len - 1

    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left = 0
        zero = 0
        zero_index = -1
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
                if zero > 1:
                    left = zero_index + 1
                    zero = 1
                zero_index = right
            max_len = max(max_len, right - left + 1)

        return max_len - 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubarray(nums = [1,1,0,1])) # 3
    print(sol.longestSubarray(nums = [0,1,1,1,0,1,1,0,1])) # 5
    print(sol.longestSubarray(nums = [1,1,1])) # 2
    print(sol.longestSubarray(nums=[0, 1, 1, 1]))  # 3
    print(sol.longestSubarray(nums=[0, 1, 1, 1, 0, 1]))  # 4
    print(sol.longestSubarray(nums=[0]))  # 0
    print(sol.longestSubarray(nums=[1, 0]))  # 1