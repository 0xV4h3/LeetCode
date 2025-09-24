# 679. 24 Game
from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        small_error = 1e-6

        def dfs(nums : List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < small_error

            for i in range(len(nums) - 1):
                for j in range(i + 1, len(nums)):
                    other_nums = []
                    for k in range(len(nums)):
                        if k != i and k != j:
                            other_nums.append(nums[k])

                    a, b = nums[i], nums[j]
                    operations = [a + b, a - b, b - a, a * b]
                    if abs(b) > small_error:
                        operations.append(a / b)
                    if abs(a) > small_error:
                        operations.append(b / a)

                    for op in operations:
                        if dfs(other_nums + [op]):
                            return True
            return False

        return dfs([float(card) for card in cards])

if __name__ == "__main__":
    sol = Solution()
    print(sol.judgePoint24(cards = [4,1,8,7])) # True ((8-4) * (7-1) = 24)
    print(sol.judgePoint24(cards = [1,2,1,2]))  # False