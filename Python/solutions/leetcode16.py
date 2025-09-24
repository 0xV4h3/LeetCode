# 16. 3Sum Closest
from typing import List
from math import inf

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = inf
        n = len(nums)

        for i in range(0, n - 2):
            left, right = i + 1, n - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if abs(three_sum - target) < abs(closest - target):
                    closest = three_sum

                if three_sum < target:
                    left += 1
                elif three_sum > target:
                    right -= 1
                else:
                    return target

        return closest

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest(nums = [-1,2,1,-4], target = 1))  # 2
    print(sol.threeSumClosest(nums = [0,0,0], target = 1))  # 0
    print(sol.threeSumClosest(nums = [4,0,5,-5,3,3,0,-4,-5], target = -2))  # -2