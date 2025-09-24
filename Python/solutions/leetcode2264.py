# 2264. Largest 3-Same-Digit Number in String
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = ''
        for i in range(1, len(num) - 1):
            if num[i - 1] == num[i] == num[i + 1]:
                good = max(good, num[i] * 3)
        return good

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestGoodInteger(num = "6777133339")) # "777"
    print(sol.largestGoodInteger(num = "2300019"))  # "000"
    print(sol.largestGoodInteger(num = "42352338"))  # ""