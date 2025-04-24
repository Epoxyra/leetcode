from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        browsed_nodes = set()
        while head != None:
            if head not in browsed_nodes:
                browsed_nodes.add(head)
            else:
                return True
            head = head.next
        return False