# 389. Find the Difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_map = dict.fromkeys(s,0)
        t_map = dict.fromkeys(t,0)
        for char in s:
            s_map[char] += 1
        for char in t:
            t_map[char] += 1
        for key in t_map:
            if key not in s_map or (key in s_map and s_map[key] != t_map[key]):
                return key
        return ''
        # t_list = list(t)
        # for char in s:
        #     t_list.remove(char)
        # return str(t_list[0])

if __name__ == "__main__":
    sol = Solution()
    example1 = sol.findTheDifference(s = "abcd", t = "abcde")
    print(example1)
    example2 = sol.findTheDifference(s = "", t = "y")
    print(example2)
    example3 = sol.findTheDifference(s = "a", t = "aa")
    print(example3)