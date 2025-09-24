# 70. Climbing Stairs
import math

class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 0
        twos = 0
        while 2 * twos <= n:
            ones = n - 2 * twos
            total = ones + twos
            ways += math.factorial(total) // (math.factorial(ones) * math.factorial(twos))
            twos += 1
        return ways

if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(n = 2)) # 2
    print(sol.climbStairs(n = 3)) # 3
    print(sol.climbStairs(n = 5))  # 8