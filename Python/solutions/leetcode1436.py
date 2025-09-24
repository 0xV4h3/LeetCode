# 1436. Destination City
from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source_city = set(b for a, b in paths)
        destination_city = set(a for a, b in paths)
        destination = (source_city - destination_city).pop()
        return destination

if __name__ == "__main__":
    sol = Solution()
    print(sol.destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))  # "Sao Paulo"
    print(sol.destCity(paths = [["B","C"],["D","B"],["C","A"]]))  # "A"
    print(sol.destCity(paths = [["A","Z"]]))  # "Z"