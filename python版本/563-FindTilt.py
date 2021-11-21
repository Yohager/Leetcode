# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        ans = 0 
        def cal_val(node):
            if not node:
                return 0 
            return node.val + cal_val(node.left) + cal_val(node.right) 
        def dfs(node):
            if not node:
                return 0
            return abs(cal_val(node.left)-cal_val(node.right)) + dfs(node.left) + dfs(node.right)
        ans = dfs(root)
        return ans