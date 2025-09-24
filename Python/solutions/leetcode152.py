# 152. Maximum Product Subarray
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = 1
        min_p = 1
        product = max(nums)

        for num in nums:
            p = max_p * num
            max_p = max(p, min_p * num, num)
            min_p = min(p, min_p * num, num)

            product = max(product, max_p)

        return product

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct(nums = [2,3,-2,4])) # 6
    print(sol.maxProduct(nums = [-2,0,-1])) # 0
