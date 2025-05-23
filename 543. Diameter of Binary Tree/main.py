from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            nonlocal diameter
            diameter = max(left_height + right_height, diameter)
            return max(left_height, right_height) + 1
        dfs(root)
        return diameter