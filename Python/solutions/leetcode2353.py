# 2353. Design a Food Rating System
import heapq
from typing import List, Dict, Tuple

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating: Dict[str, int] = {f: r for f, r in zip(foods, ratings)}
        self.food_cuisine: Dict[str, str] = dict(zip(foods, cuisines))
        self.cuisine_heaps: Dict[str, List[Tuple[int, str]]] = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.cuisine_heaps.setdefault(c, []).append((-r, f))

        for heap in self.cuisine_heaps.values():
            heapq.heapify(heap)

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = newRating
        cuisine = self.food_cuisine[food]
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]
        while heap and -heap[0][0] != self.food_rating[heap[0][1]]:
            heapq.heappop(heap)
        return heap[0][1]

if __name__ == "__main__":
    food1 = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])
    print(food1.highestRated("korean")) # "kimchi"
    print(food1.highestRated("japanese")) # "ramen"
    food1.changeRating("sushi", 16)
    print(food1.highestRated("japanese")) # "sushi"
    food1.changeRating("ramen", 16)
    print(food1.highestRated("japanese")) # "ramen"

