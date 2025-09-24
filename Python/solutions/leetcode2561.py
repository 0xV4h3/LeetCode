# 2561. Rearranging Fruits
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        fruit_types = {}

        for i in range(len(basket1)):
            fruit1 = basket1[i]
            fruit2 = basket2[i]

            if fruit1 in fruit_types:
                fruit_types[fruit1] += 1
            else:
                fruit_types[fruit1] = 1

            if fruit2 in fruit_types:
                fruit_types[fruit2] -= 1
            else:
                fruit_types[fruit2] = -1

        min_fruit_type = float('inf')
        for fruit in basket1 + basket2:
            if fruit < min_fruit_type:
                min_fruit_type = fruit

        exchange_list = []
        for fruit in fruit_types:
            count = fruit_types[fruit]
            if count % 2 != 0:
                return -1
            exchange_times = abs(count) // 2
            for _ in range(exchange_times):
                exchange_list.append(fruit)

        exchange_list.sort()

        total_cost = 0
        n = len(exchange_list) // 2
        for i in range(n):
            cost = min(exchange_list[i], 2 * min_fruit_type)
            total_cost += cost

        return total_cost

if __name__ == "__main__":
    sol = Solution()
    example1 = sol.minCost(basket1 = [4,2,2,2], basket2 = [1,4,1,2])
    print(example1)
    example2 = sol.minCost(basket1 = [2,3,4,1], basket2 = [3,2,5,1])
    print(example2)