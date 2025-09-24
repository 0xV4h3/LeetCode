# 342. Power of Four
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and ((n & (n - 1)) == 0) and ((n & 0xAAAAAAAA) == 0)

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfFour(n = 16)) # True
    print(sol.isPowerOfFour(n = 5))  # False
    print(sol.isPowerOfFour(n = 1))  # True