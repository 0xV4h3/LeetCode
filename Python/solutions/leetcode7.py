# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x

        number = str(abs(x))
        result = int(number[::-1])

        if x > 0 and result < (2 ** 31) - 1:
            return result
        elif x < 0 and result < 2 ** 31:
            return -result

        return 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(x = 123)) # 321
    print(sol.reverse(x = -123)) # -321
    print(sol.reverse(x = 120))  # 21
    print(sol.reverse(x = 0))  # 0
    print(sol.reverse(x = -2147483648))  # 0