# 165. Compare Version Numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        n = max(len(v1), len(v2))

        for i in range(n):
            num1 = v1[i] if i < len(v1) else 0
            num2 = v2[i] if i < len(v2) else 0
            if num1 < num2:
                return -1
            if num1 > num2:
                return 1
        return 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.compareVersion(version1 = "1.2", version2 = "1.10")) # -1
    print(sol.compareVersion(version1 = "1.01", version2 = "1.001")) # 0
    print(sol.compareVersion(version1 = "1.0", version2 = "1.0.0.0")) # 0