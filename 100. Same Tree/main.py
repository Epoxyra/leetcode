from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        if (q and not p) or (p and not q):
            return False
        elif not q and not p:
            return True
        
        queue.append(q)
        queue.append(p)

        while queue:
            q_node = queue.popleft()
            p_node = queue.popleft()

            if q_node.val != p_node.val:
                return False
            if (q_node.left and not p_node.left) or (p_node.left and not q_node.left) or (q_node.right and not p_node.right) or (p_node.right and not q_node.right):
                return False
            if (q_node.left and p_node.left):
                queue.append(q_node.left)
                queue.append(p_node.left)
            if (q_node.right and p_node.right):
                queue.append(q_node.right)
                queue.append(p_node.right)

        return True