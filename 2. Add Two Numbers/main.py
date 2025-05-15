from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = l1
        l1_numbers = []
        while node:
            l1_numbers.append(node.val)
            node = node.next
        
        node = l2
        l2_numbers = []
        while node:
            l2_numbers.append(node.val)
            node = node.next

        l1_numbers = l1_numbers[::-1]
        l2_numbers = l2_numbers[::-1]

        l1_str = "".join([str(x) for x in l1_numbers])
        l2_str = "".join([str(x) for x in l2_numbers])
        res_str = str(int(l1_str) + int(l2_str))
        res_numbers = [int(digit) for digit in res_str][::-1]

        head = ListNode()
        node = head
        for i in range(len(res_numbers)):
            node.val = res_numbers[i]
            if i + 1 <= len(res_numbers) - 1:
                node.next = ListNode()
            node = node.next
        
        return head
