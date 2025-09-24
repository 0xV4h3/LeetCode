# 869. Reordered Power of 2
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return sorted(str(n)) in (sorted(str(1 << i)) for i in range(30))

if __name__ == "__main__":
    sol = Solution()
    print(sol.reorderedPowerOf2(n = 1)) # True
    print(sol.reorderedPowerOf2(n = 10)) # False