# 2785. Sort Vowels in a String
class Solution:
    def sortVowels(self, s: str) -> str:
        v = "aeiouAEIOU"
        t = ''
        vowels = []
        for c in s:
            if c in v:
                vowels.append(c)

        vowels.sort(reverse=True)
        for c in s:
            t += vowels.pop() if c in v else c

        return t

if __name__ == "__main__":
    sol = Solution()
    print(sol.sortVowels(s = "lEetcOde"))  # "lEOtcede"
    print(sol.sortVowels(s = "lYmpH"))  # "lYmpH"