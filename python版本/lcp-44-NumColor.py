# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def numColor(self, root: TreeNode) -> int:
        res = set()
        def dfs(node):
            nonlocal res
            if not node:
                return 
            res.add(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return len(res)