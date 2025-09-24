# 3021. Alice and Bob Playing Flower Game

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (m * n) // 2

if __name__ == "__main__":
    sol = Solution()
    print(sol.flowerGame(n = 3, m = 2)) # 3
    print(sol.flowerGame(n = 1, m = 1)) # 0