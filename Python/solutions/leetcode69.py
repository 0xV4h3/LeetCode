# 69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l = 0
        r = x // 2
        while l <= r:
            mid = l + (r - l) // 2
            square = mid * mid
            if square == x or (square < x < (mid + 1) * (mid + 1)):
                return mid
            elif square < x:
                l = mid + 1
            elif square > x:
                r = mid - 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(x = 4)) # 2
    print(sol.mySqrt(x = 8))  # 2
    print(sol.mySqrt(x = 0))  # 0