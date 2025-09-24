# 2. Add Two Numbers
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def linked_to_string(head: ListNode) -> str:
            result = ''
            current = head
            while current:
                result += (str(current.val))
                current = current.next
            return result

        number1 = int(linked_to_string(l1)[::-1])
        number2 = int(linked_to_string(l2)[::-1])

        summ = number1 + number2
        if summ == 0:
            return ListNode(0)

        result = ListNode()
        curr = result
        while summ > 0:
            curr.next = ListNode(summ % 10)
            curr = curr.next
            summ //= 10

        return result.next

def list_to_linked(lst):
    head = ListNode()
    curr = head
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return head.next

def linked_to_list(head: ListNode) -> list[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    sol = Solution()
    l1 = list_to_linked([2,4,3])
    l2 = list_to_linked([5, 6, 4])
    print(linked_to_list(sol.addTwoNumbers(l1, l2))) # [7,0,8]
    l1 = list_to_linked([0])
    l2 = list_to_linked([0])
    print(linked_to_list(sol.addTwoNumbers(l1, l2))) # [0]
    l1 = list_to_linked([9,9,9,9,9,9,9])
    l2 = list_to_linked([9,9,9,9])
    print(linked_to_list(sol.addTwoNumbers(l1, l2))) # [8,9,9,9,0,0,0,1]