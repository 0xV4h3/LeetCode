# 1656. Design an Ordered Stream
from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.next_id = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.stream[idKey] = value
        if idKey != self.next_id:
            return []

        res = []
        while self.next_id < len(self.stream) and self.stream[self.next_id] is not None:
            res.append(self.stream[self.next_id])
            self.next_id += 1
        return res

if __name__ == "__main__":
    stream = OrderedStream(5)
    print(stream.insert(3, "ccccc")) # []
    print(stream.insert(1, "aaaaa")) # ["aaaaa"]
    print(stream.insert(2, "bbbbb")) # ["bbbbb", "ccccc"]
    print(stream.insert(5, "eeeee")) # []
    print(stream.insert(4, "ddddd")) # ["ddddd", "eeeee"]