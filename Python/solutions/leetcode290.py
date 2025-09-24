# 290. Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = list(s.split(' '))
        if len(pattern) != len(words):
            return False
        pattern_match = {}
        word_match = {}
        for i in range(len(pattern)):
            if pattern[i] in pattern_match and words[i] in word_match:
                if pattern_match[pattern[i]] != words[i] and word_match[words[i]] != pattern[i]:
                    return False
            elif (pattern[i] not in pattern_match and words[i] in word_match) or (pattern[i] in pattern_match and words[i] not in word_match):
                return False
            else:
                pattern_match[pattern[i]] = words[i]
                word_match[words[i]] = pattern[i]
        return True

if __name__ == "__main__":
    sol = Solution()
    example1 = sol.wordPattern(pattern = "abba", s = "dog cat cat dog")
    print(example1)
    example2 = sol.wordPattern(pattern = "abba", s = "dog cat cat fish")
    print(example2)
    example3 = sol.wordPattern(pattern = "aaaa", s = "dog cat cat dog")
    print(example3)
    example4 = sol.wordPattern(pattern = "abba", s = "dog dog dog dog")
    print(example4)