# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = False 
        def dfs(node,val):
            nonlocal ans 
            if not node:
                return 
            if not node.left and not node.right:
                if val == node.val:
                    ans = True
            dfs(node.left,val-node.val)
            dfs(node.right,val-node.val)
        if not root:
            return False 
        dfs(root,targetSum)
        return ans 
 