# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return True, 0
            left_balanced, left_height = dfs(root.left)
            right_balanced, right_height = dfs(root.right)
            node_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            return node_balanced, max(left_height, right_height) + 1
        is_balanced, _ = dfs(root)
        return is_balanced
    

                    

