from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        all_nodes = []
        node = head
        
        while node:
            tmp = node.next
            node.next = None
            all_nodes.append(node)
            node = tmp
        # Si la liste est vide, retournez None
        if not all_nodes:
            return None
        reversed_list = all_nodes[-1]
        res = reversed_list
        for i in range(len(all_nodes) - 2, -1, -1):
            reversed_list.next = all_nodes[i]
            reversed_list = reversed_list.next
        return res