# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left, right = 0, 0
        while right < len(s):
            if s[right] in s[left:right]:
                while s[right] in s[left:right] and left != right:
                    left += 1
            else:
                max_len = max(max_len, right - left + 1)
                right += 1

        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s = "abcabcbb")) # 3
    print(sol.lengthOfLongestSubstring(s = "bbbbb")) # 1
    print(sol.lengthOfLongestSubstring(s = "pwwkew"))  # 3