# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        def func1(node):
            if not node:
                return 0
            return func1(node.left) + func1(node.right) + 1
        
        def func2(node):
            if not node:
                return 0 
            return func2(node.left) + func2(node.right) + node.val
        
        # print(func1(root),func2(root))
        
        def dfs(node):
            nonlocal ans 
            if not node:
                return 
            cnt,v = func1(node), func2(node)
            if v // cnt == node.val:
                ans += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ans 
            
            