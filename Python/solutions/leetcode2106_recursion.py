# 2561. Rearranging Fruits
from typing import List
import copy

class Solution:
    def canReach(self, fruits: List[List[int]], Pos: int, k: int) -> List[List[int]]:
        reachable_fruit = []
        for fruit in fruits:
            if abs(fruit[0] - Pos) <= k:
                reachable_fruit.append(fruit)
        return reachable_fruit

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        fruits_reachable = self.canReach(fruits, startPos, k)

        if not fruits_reachable:
            return 0

        harvested = []

        for fruit in fruits_reachable:
            fruits_after = copy.deepcopy(fruits_reachable)
            fruits_after.remove(fruit)

            remaining_k = k - abs(fruit[0] - startPos)
            harvested_fruit = fruit[1] + self.maxTotalFruits(fruits_after, fruit[0], remaining_k)
            harvested.append(harvested_fruit)

        return max(harvested) if harvested else 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxTotalFruits([[2,8],[6,3],[8,6]], startPos=5, k=4))
    print(sol.maxTotalFruits([[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos=5, k=4))
    print(sol.maxTotalFruits([[0,3],[6,4],[8,5]], startPos=3, k=2))
    print(sol.maxTotalFruits([[20000, 10000]], startPos=20000, k=0))