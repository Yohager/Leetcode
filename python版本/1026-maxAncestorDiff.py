# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, maxv, minv):
            if not node: 
                nonlocal ans 
                ans = max(ans, maxv - minv)
                return 
            maxv = max(maxv, node.val)
            minv = min(minv, node.val)
            dfs(node.left, maxv, minv)
            dfs(node.right, maxv, minv)
        dfs(root, root.val, root.val)
        return ans 
        
        
