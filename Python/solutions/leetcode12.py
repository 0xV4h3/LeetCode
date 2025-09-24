# 12. Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ''
        for i in range(len(num_list)):
            while num >= num_list[i] and num != 0:
                roman += roman_list[i]
                num -= num_list[i]
            if num == 0:
                break
        return roman

if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(num = 3749)) # "MMMDCCXLIX"
    print(sol.intToRoman(num = 58))  # "LVIII"
    print(sol.intToRoman(num = 1994))  # "MCMXCIV"