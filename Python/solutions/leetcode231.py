# 231. Power of Two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfTwo(n = 1)) # True
    print(sol.isPowerOfTwo(n = 16)) # True
    print(sol.isPowerOfTwo(n = 3))  # False