# 17. Letter Combinations of a Phone Number
from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keypad = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        combinations = ["".join(p) for p in product(*(keypad[d] for d in digits))]
        return combinations

if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations(digits = "23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(sol.letterCombinations(digits = ""))  # []
    print(sol.letterCombinations(digits = "2"))  # ["a","b","c"]