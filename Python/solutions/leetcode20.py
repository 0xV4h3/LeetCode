# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []

        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            else:
                if stack:
                    last = stack.pop()
                    if bracket != brackets[last]:
                        return False
                else:
                    return False

        return not stack

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid(s = "()")) # True
    print(sol.isValid(s = "()[]{}")) # True
    print(sol.isValid(s = "(]")) # False
    print(sol.isValid(s = "([])"))  # True
    print(sol.isValid(s = "([)]")) # False
    print(sol.isValid(s = "){")) # False

