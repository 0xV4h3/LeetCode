# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(x = 121)) # True
    print(sol.isPalindrome(x = -121))  # False
    print(sol.isPalindrome(x = 10))  # False