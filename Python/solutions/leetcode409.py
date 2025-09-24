# 409. Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_map = {}
        length = 0
        has_odd = False

        for letter in s:
            letter_map[letter] = letter_map.get(letter, 0) + 1

        for l in letter_map.values():
            if l % 2 == 0:
                length += l
            else:
                length += l - 1
                has_odd = True

        return length + (1 if has_odd else 0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome(s = "abccccdd"))  # 7
    print(sol.longestPalindrome(s = "a"))  # 1