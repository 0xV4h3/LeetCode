# 898. Bitwise ORs of Subarrays
class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        unique_or_results = set()
        prev = 0
        for index, value in enumerate(arr):
            prev |= value
            current = 0
            for j in range(index, -1, -1):
                current |= arr[j]
                unique_or_results.add(current)
                if current == prev:
                    break
        return len(unique_or_results)

if __name__ == "__main__":
    sol = Solution()
    example1 = sol.subarrayBitwiseORs(arr = [0])
    print(example1)
    example2 = sol.subarrayBitwiseORs(arr = [1,1,2])
    print(example2)
    example3 = sol.subarrayBitwiseORs([1,2,4])
    print(example3)