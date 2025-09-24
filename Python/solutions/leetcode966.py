# 966. Vowel Spellchecker
from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def deVowel(s):
            return ''.join('*' if c in 'aeiou' else c for c in s)

        exact = set(wordlist)
        case = {}
        vowel = {}

        for w in wordlist:
            low = w.lower()
            case.setdefault(low, w)
            vowel.setdefault(deVowel(low), w)

        answer = []

        for q in queries:
            if q in exact:
                answer.append(q)
            else:
                lower = q.lower()
                devowel = deVowel(lower)
                if lower in case:
                    answer.append(case[lower])
                elif devowel in vowel:
                    answer.append((vowel[devowel]))
                else:
                    answer.append('')

        return answer

if __name__ == "__main__":
    sol = Solution()
    print(sol.spellchecker(wordlist = ["KiTe","kite","hare","Hare"],
                           queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))
    # ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
    print(sol.spellchecker(wordlist = ["yellow"], queries = ["YellOw"])) # ["yellow"]