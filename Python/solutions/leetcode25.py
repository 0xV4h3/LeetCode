# 25. Reverse Nodes in k-Group
from typing import Optional, Tuple

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = ListNode()
        new_head.next = head
        prev_group = new_head

        while head:
            if self.canReverse(head, k):
                k_group_end = head
                for _ in range(k - 1):
                    k_group_end = k_group_end.next
                next_group = k_group_end.next
                k_group_end.next = None
                new_group_head = self.reverseList(head)

                prev_group.next = new_group_head
                head.next = next_group

                prev_group = head
                head = next_group
            else:
                break

        return new_head.next

    def canReverse(self, node: Optional[ListNode], k: int) -> bool:
        curr = node
        count = 0
        while count < k and curr:
            curr = curr.next
            count += 1
        return count == k

    def reverseList(self, node: Optional[ListNode]) -> Optional[ListNode]:
        curr = node
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

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
    l1 = list_to_linked([1, 2, 3, 4, 5])
    print(linked_to_list(sol.reverseKGroup(l1, k = 2))) # [2,1,4,3,5]
    l2 = list_to_linked([1, 2, 3, 4, 5])
    print(linked_to_list(sol.reverseKGroup(l2, k = 3))) # [3,2,1,4,5]