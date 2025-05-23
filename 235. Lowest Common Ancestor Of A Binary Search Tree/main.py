# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = root
        def dfs(head):
            nonlocal lca
            if not head:
                return False
            l_bool = dfs(head.left)
            r_bool = dfs(head.right)
            head_bool = True if head.val == q.val or head.val == p.val else False
            if (l_bool and r_bool) or (head_bool and l_bool) or (head_bool and r_bool):
                lca = head
            if head_bool:
                return True
            return l_bool or r_bool
        dfs(root)
        return lca

