# 8. String to Integer (atoi)
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if s == '':
            return 0
        is_negative = False
        result = ''
        if s[0] == '-':
            is_negative = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        for symbol in s:
            if symbol == '0' and result == '':
                continue
            if symbol.isdigit():
                result += symbol
            else:
                break

        if result == '':
            return 0

        INT_MIN = -(2 ** 31)
        INT_MAX = (2 ** 31) - 1

        num = -int(result) if is_negative else int(result)

        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX
        return num

if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi(s = "42")) # 42
    print(sol.myAtoi(s = " -042")) # -42
    print(sol.myAtoi(s = "1337c0d3"))  # 1337
    print(sol.myAtoi(s = "0-1"))  # 0
    print(sol.myAtoi(s = "words and 987"))  # 0