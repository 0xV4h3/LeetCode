# 858. Mirror Reflection
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        from math import gcd
        lcm = p * q // gcd(p, q)
        m = lcm // q
        n = lcm // p
        if m % 2 == 0:
            return 2
        elif n % 2 == 0:
            return 0
        else:
            return 1

if __name__ == "__main__":
    sol = Solution()
    case1 = sol.mirrorReflection(2,1)
    case2 = sol.mirrorReflection(3,1)
    case3 = sol.mirrorReflection(3,2)
    print(f"Input: 2, 1\nOutput: {case1}")
    print(f"Input: 3, 1\nOutput: {case2}")
    print(f"Input: 3, 2\nOutput: {case3}")