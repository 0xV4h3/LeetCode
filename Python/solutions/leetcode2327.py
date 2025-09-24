# 2327. Number of People Aware of a Secret

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1

        for day in range(1, n + 1):
            sharers = dp[day]
            for d in range(day + delay, min(n, day + forget - 1) + 1):
                dp[d] = (dp[d] + sharers) % MOD

        people = 0
        for day in range(n - forget + 1, n + 1):
            people = (people + dp[day]) % MOD

        return people

if __name__ == "__main__":
    sol = Solution()
    print(sol.peopleAwareOfSecret(n = 6, delay = 2, forget = 4))  # 5
    print(sol.peopleAwareOfSecret(n = 4, delay = 1, forget = 3))  # 6
