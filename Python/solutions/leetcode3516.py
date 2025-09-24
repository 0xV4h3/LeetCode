# 3516. Find Closest Person

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        first = abs(z - x)
        second = abs(z - y)
        if first < second:
            return 1
        elif first > second:
            return 2
        return 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.findClosest(x = 2, y = 7, z = 4))  # 1
    print(sol.findClosest(x = 2, y = 5, z = 6))  # 2
    print(sol.findClosest(x = 1, y = 5, z = 3))  # 0