# 32. Longest Valid Parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestValidParentheses(s = "(()")) # 2
    print(sol.longestValidParentheses(s = ")()())")) # 4
    print(sol.longestValidParentheses(s = ""))  # 0