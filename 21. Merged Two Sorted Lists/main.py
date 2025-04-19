# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        tail = res
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next
        tail.next = list1 or list2
        return res.next

list1 = ListNode(1)
list2 = ListNode(1)
list1.next = ListNode(2)
list2.next = ListNode(3)
list1.next.next = ListNode(4)
list2.next.next = ListNode(4)
solution_instance = Solution()
res = solution_instance.mergeTwoLists(list1, list2)
while res.next is not None:
    print(res.val)
    res = res.next