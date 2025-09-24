# 326. Power of Three
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3

        return n == 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfThree(n = 27)) # True
    print(sol.isPowerOfThree(n = 0)) # False
    print(sol.isPowerOfThree(n = -1)) # False
