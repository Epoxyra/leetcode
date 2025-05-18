from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left_tree, right_tree):
            if not left_tree and not right_tree:
                return True
            l_val = left_tree.val if left_tree else None
            r_val = right_tree.val if right_tree else None
            if l_val != r_val:
                return False
            return dfs(left_tree.left, right_tree.right) and dfs(right_tree.left, left_tree.right)
        return dfs(root.left, root.right)