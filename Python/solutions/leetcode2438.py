# 2438. Range Product Queries of Powers
from typing import List
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        modulo = 10 ** 9 + 7

        powers = []
        place = 1
        while n > 0:
            if n % 2 == 1:
                powers.append(place)
            n //= 2
            place *= 2

        result = []
        for left, right in queries:
            power = 1
            for i in range(left, right + 1):
                power = power * powers[i] % modulo
            result.append(power)

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.productQueries(n = 15, queries = [[0,1],[2,2],[0,3]])) # [2,4,64]
    print(sol.productQueries(n = 2, queries = [[0,0]])) # [2]
