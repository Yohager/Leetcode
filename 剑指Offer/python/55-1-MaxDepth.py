# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        paths = []
        tmp = []
        def dfs(node):
            if not node:
                return 
            tmp.append(node.val)
            if not node.left and not node.right:
                paths.append(tmp[:])
            dfs(node.left)
            dfs(node.right)
            tmp.pop()
        dfs(root)
        ans = 0
        for i in paths:
            ans = max(ans,len(i))
        return ans