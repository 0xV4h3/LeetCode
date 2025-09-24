# 2787. Ways to Express an Integer as Sum of Powers
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MODULO = (10 ** 9) + 7
        powers = []
        i = 1
        while True:
            power = i ** x
            if power > n:
                break
            powers.append(power)
            i += 1

        dp = [0] * (n + 1)
        dp[0] = 1
        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MODULO

        return dp[n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfWays(n = 10, x = 2)) # 1
    print(sol.numberOfWays(n = 4, x = 1)) # 2