# 3477. Fruits Into Baskets II
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        unplaced = n
        sector_size = int(n ** 0.5)
        sector_max = []
        sectors = 0
        for i in range(0, n, sector_size):
            sector_max.append(max(baskets[i:i + sector_size]))
            sectors += 1

        for i in range(n):
            for j in range(sectors):
                if sector_max[j] >= fruits[i]:
                    start = j * sector_size
                    end = (j + 1) * sector_size
                    for k in range(start, end):
                        if baskets[k] >= fruits[i]:
                            if baskets[k] == sector_max[j]:
                                baskets[k] = 0
                                sector_max[j] = max(baskets[start:end])
                            else:
                                baskets[k] = 0
                            unplaced -= 1
                            break
                    break
        return  unplaced

if __name__ == "__main__":
    sol = Solution()
    print(sol.numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4]))
    print(sol.numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7]))