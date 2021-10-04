# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @lru_cache()
    def isValidBST(self, root: TreeNode) -> bool:
        # ans = []
        # def mid_order(node):
        #     nonlocal ans 
        #     if not node:
        #         return 
        #     mid_order(node.left)
        #     ans.append(node.val)
        #     mid_order(node.right)
        # mid_order(root)
        # for i in range(1,len(ans)):
        #     if ans[i] <= ans[i-1]:
        #         return False
        # return True
        def dfs(node,val1,val2):
            if not node:
                return True 
            if not (val1 < node.val < val2):
                return False 
            return dfs(node.left,val1,node.val) and dfs(node.right,node.val,val2)
        return dfs(root,-float('inf'),float('inf'))
