#13 Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        number = roman[s[0]]
        for i in range(1, len(s)):
            current = roman[s[i]]
            previous = roman[s[i - 1]]
            if current <= previous:
                number += current
            elif current / previous == 5 or current / previous == 10:
                number += current - (2 * previous)
            else:
                print("Invalid roman number")
        return number

if __name__ == "__main__":
    sol = Solution()
    case1 = sol.romanToInt("III")
    case2 = sol.romanToInt("LVIII")
    case3 = sol.romanToInt("MCMXCIV")
    print(f"Input: III\nOutput: {case1}")
    print(f"Input: LVIII\nOutput: {case2}")
    print(f"Input: MCMXCIV\nOutput: {case3}")