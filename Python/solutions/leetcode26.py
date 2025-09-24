# 26. Remove Duplicates from Sorted Array
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0

        for i in range(len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]

        return index+1

        # n = len(nums)
        # if n == 0:
        #     return 0
        #
        # i = 1
        # while i < len(nums):
        #     if nums[i] == nums[i - 1]:
        #         nums.pop(i)
        #     else:
        #         i += 1
        #
        # return len(nums)

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates(nums = [1,1,2]))  # 2
    print(sol.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))  # 5
