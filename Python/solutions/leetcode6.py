# 6. Zigzag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        conversion = [''] * numRows
        row = 0
        i = 0

        while i < len(s):
            conversion[row] += s[i]
            row = min(numRows - 1, row + 1)
            i += 1
            if row == numRows - 1:
                while row != 0 and i < len(s):
                    conversion[row] += s[i]
                    row = max(0, row - 1)
                    i += 1

        return ''.join(conversion)

if __name__ == "__main__":
    sol = Solution()
    print(sol.convert(s = "PAYPALISHIRING", numRows = 3)) # "PAHNAPLSIIGYIR"
    print(sol.convert(s = "PAYPALISHIRING", numRows = 4))  # "PINALSIGYAHRPI"
    print(sol.convert(s = "A", numRows = 1))  # "A"
    print(sol.convert(s = "AB", numRows = 1))  # "AB"