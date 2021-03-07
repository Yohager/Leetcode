# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sums: int) -> List[List[int]]:
        ans = []
        tmp = []
        def dfs(node,val):
            if not node:
                return 
            tmp.append(node.val)
            val -= node.val
            if not node.left and not node.right and val == 0:
                ans.append(list(tmp))
            dfs(node.left, val)
            dfs(node.right,val)
            tmp.pop()
        dfs(root,sums)
        return ans 