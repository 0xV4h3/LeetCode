# 3508. Implement Router
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right

class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.q = deque()
        self.seen = set()
        self.dest_map = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.seen:
            return False
        if len(self.q) == self.limit:
            s, d, t = self.q.popleft()
            self.seen.remove((s, d, t))
            lst = self.dest_map[d]
            if lst and lst[0] == t:
                lst.pop(0)
            else:
                idx = bisect_left(lst, t)
                if idx < len(lst) and lst[idx] == t:
                    lst.pop(idx)

        self.q.append(key)
        self.seen.add(key)
        self.dest_map[destination].append(timestamp)
        return True

    def forwardPacket(self):
        if not self.q:
            return []
        s, d, t = self.q.popleft()
        self.seen.remove((s, d, t))
        lst = self.dest_map[d]
        if lst and lst[0] == t:
            lst.pop(0)
        else:
            idx = bisect_left(lst, t)
            if idx < len(lst) and lst[idx] == t:
                lst.pop(idx)
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        lst = self.dest_map[destination]
        left = bisect_left(lst, startTime)
        right = bisect_right(lst, endTime)
        return right - left

if __name__ == "__main__":
    router = Router(3)
    print(router.addPacket(1, 4, 90)) # True
    print(router.addPacket(2, 5, 90)) # True
    print(router.addPacket(1, 4, 90)) # False
    print(router.addPacket(3, 5, 95)) # True
    print(router.addPacket(4, 5, 105)) # True
    print(router.forwardPacket()) # [2, 5, 90]
    print(router.addPacket(5, 2, 110)) # True
    print(router.getCount(5, 100, 110)) # 1

