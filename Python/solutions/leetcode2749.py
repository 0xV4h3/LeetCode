# 2749. Minimum Operations to Make the Integer Zero
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_count():
                return k
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.makeTheIntegerZero(num1 = 3, num2 = -2))  # 3
    print(sol.makeTheIntegerZero(num1 = 5, num2 = 7))  # -1