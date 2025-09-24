# 1935. Maximum Number of Words You Can Type

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = 0
        broken = False
        for ch in text:
            if ch == ' ':
                if not broken:
                    words += 1
                broken = False
            elif not broken and ch in brokenLetters:
                broken = True
        if not broken:
            words += 1
        return words

if __name__ == "__main__":
    sol = Solution()
    print(sol.canBeTypedWords(text = "hello world", brokenLetters = "ad"))  # 1
    print(sol.canBeTypedWords(text = "leet code", brokenLetters = "lt"))  # 1
    print(sol.canBeTypedWords(text = "leet code", brokenLetters = "e"))  # 0