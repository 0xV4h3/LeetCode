# 30. Substring with Concatenation of All Words
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        n = len(s)

        words_map = {}
        for w in words:
            words_map[w] = words_map.get(w, 0) + 1

        result = []

        for offset in range(word_len):
            left = offset
            right = offset
            current_count = {}
            count = 0

            while right + word_len <= n:
                word = s[right:right + word_len]
                right += word_len

                if word in words_map:
                    current_count[word] = current_count.get(word, 0) + 1
                    count += 1

                    while current_count[word] > words_map[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        result.append(left)
                else:
                    current_count.clear()
                    count = 0
                    left = right

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))  # [0,9]
    print(sol.findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]))  # []
    print(sol.findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]))  # [6,9,12]
    print(sol.findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","good"]))  # [8]
    print(sol.findSubstring(s = "lingmindraboofooowingdingbarrwingmonkeypoundcake", words = ["fooo","barr","wing","ding","wing"]))  # [13]