from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        node = head
        while node:
            counter += 1
            node = node.next
        middle = counter // 2
        for _ in range(middle):
            head = head.next
        return head
            