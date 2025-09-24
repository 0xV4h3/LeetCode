# 21. Merge Two Sorted Lists
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head

        cur1, cur2 = list1, list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                tail.next = cur1
                cur1 = cur1.next
            else:
                tail.next = cur2
                cur2 = cur2.next
            tail = tail.next

        tail.next = cur1 if cur1 else cur2

        return head.next

def list_to_linked(lst: list[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode()
    curr = head
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return head.next

def linked_to_list(head: Optional[ListNode]) -> list[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


if __name__ == "__main__":
    sol = Solution()
    l1 = list_to_linked([1, 2, 4])
    l2 = list_to_linked([1, 3, 4])
    print(linked_to_list(sol.mergeTwoLists(l1, l2))) # [1,1,2,3,4,4]

    l1 = list_to_linked([])
    l2 = list_to_linked([])
    print(linked_to_list(sol.mergeTwoLists(l1, l2))) # []

    l1 = list_to_linked([])
    l2 = list_to_linked([0])
    print(linked_to_list(sol.mergeTwoLists(l1, l2))) # [0]
