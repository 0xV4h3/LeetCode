# 2197. Replace Non-Coprime Numbers in Array
from typing import List
from math import gcd, lcm

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack:
                g = gcd(stack[-1], num)
                if g == 1:
                    break
                num = lcm(stack.pop(), num)
            stack.append(num)

        return stack

if __name__ == "__main__":
    sol = Solution()
    print(sol.replaceNonCoprimes(nums = [6,4,3,2,7,6,2]))  # [12,7,6]
    print(sol.replaceNonCoprimes(nums = [2,2,1,1,3,3,3]))  # [2,1,1,3]