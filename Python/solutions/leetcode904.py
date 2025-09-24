# 904. Fruit Into Baskets
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = 0
        max_fruit = 0

        for right, x in enumerate(fruits):
            count[x] = count.get(x, 0) + 1

            while len(count) > 2:
                y = fruits[left]
                count[y] -= 1
                if count[y] == 0:
                    del count[y]
                left += 1

            max_fruit = max(max_fruit, right - left + 1)

        return max_fruit

if __name__ == "__main__":
    sol = Solution()
    print(sol.totalFruit(fruits = [1,2,1]))
    print(sol.totalFruit(fruits = [0,1,2,2]))
    print(sol.totalFruit(fruits = [1,2,3,2,2]))