# 3408. Design Task Manager
import heapq
from typing import List, Dict, Tuple

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_info: Dict[int, Tuple[int, int]] = {}
        self.heap: List[Tuple[int, int, int]] = []

        for user, task, pr in tasks:
            self.task_info[task] = (user, pr)
            heapq.heappush(self.heap, (-pr, -task, user))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_info[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        user, _ = self.task_info[taskId]
        self.task_info[taskId] = (user, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, user))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_info:
            del self.task_info[taskId]

    def execTop(self) -> int:
        while self.heap:
            pr, neg_task, user = self.heap[0]
            task = -neg_task
            if task not in self.task_info:
                heapq.heappop(self.heap)
                continue
            u, p = self.task_info[task]
            if p != -pr:
                heapq.heappop(self.heap)
                continue
            heapq.heappop(self.heap)
            del self.task_info[task]
            return u
        return -1

if __name__ == "__main__":
    manager = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
    manager.add(4, 104, 5)
    manager.edit(102, 8)
    print(manager.execTop()) # 3
    manager.rmv(101)
    manager.add(5, 105, 15)
    print(manager.execTop()) # 5