# 23. Merge k Sorted Lists
from typing import Optional, List, Tuple
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(N log k) time - O(k) space
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap: List[Tuple[int, int, ListNode]] = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        head = ListNode()
        tail = head

        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return head.next

    # O(N log N) time - O(N) space
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     priority_queue = []
    #     head = ListNode()
    #     tail = head
    #
    #     for node in lists:
    #         if not node:
    #             continue
    #         current = node
    #         while current:
    #             heapq.heappush(priority_queue, current.val)
    #             current = current.next
    #
    #     while priority_queue:
    #         tail.next = ListNode(heapq.heappop(priority_queue))
    #         tail = tail.next
    #
    #     return head.next

def list_to_linked_multi(lists: List[List[int]]) -> List[Optional[ListNode]]:
    result: List[Optional[ListNode]] = []
    for lst in lists:
        if not lst:
            result.append(None)
            continue
        head = ListNode()
        curr = head
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        result.append(head.next)
    return result

def linked_to_list(head: Optional[ListNode]) -> list[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    sol = Solution()
    lists  = list_to_linked_multi([[1,4,5],[1,3,4],[2,6]])
    print(linked_to_list(sol.mergeKLists(lists))) # [1,1,2,3,4,4,5,6]

    lists  = list_to_linked_multi([])
    print(linked_to_list(sol.mergeKLists(lists))) # []

    lists  = list_to_linked_multi([[]])
    print(linked_to_list(sol.mergeKLists(lists))) # []

