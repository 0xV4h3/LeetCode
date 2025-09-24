# 1912. Design Movie Rental System
from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.price_map = {}
        self.available_per_movie = defaultdict(SortedList)
        self.rented = SortedList()

        for shop, movie, price in entries:
            self.price_map[(shop, movie)] = price
            self.available_per_movie[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        return [shop for price, shop in self.available_per_movie[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self.available_per_movie[movie].discard((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self.rented.discard((price, shop, movie))
        self.available_per_movie[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for price, shop, movie in self.rented[:5]]

if __name__ == "__main__":
    movieRentingSystem = MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]])
    print(movieRentingSystem.search(1)) # [1, 0, 2]
    movieRentingSystem.rent(0, 1)
    movieRentingSystem.rent(1, 2)
    print(movieRentingSystem.report()) # [[0, 1], [1, 2]]
    movieRentingSystem.drop(1, 2)
    print(movieRentingSystem.search(2)) # [0, 1]
