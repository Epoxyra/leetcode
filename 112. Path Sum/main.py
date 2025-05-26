from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = deque()
        queue.append(root)
        path_sum = []

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    path_sum.append(node.val)
                if node.left:
                    node.left.val += node.val
                    queue.append(node.left)
                if node.right:
                    node.right.val += node.val
                    queue.append(node.right)
        for sum in path_sum:
            if sum == targetSum:
                return True
        return False