# 50. Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(x = 2.00000, n = 10))  # 1024.00000
    print(sol.myPow(x = 2.10000, n = 3))  # 9.26100
    print(sol.myPow(x = 2.00000, n = -2))  # 0.25000