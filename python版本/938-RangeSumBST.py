# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = []
        def order(rootnode,ans):
            if not rootnode:
                return 
            order(rootnode.left,ans)
            if rootnode.val >= low and rootnode.val <= high:
                #print(rootnode.val)
                ans.append(rootnode.val)
            order(rootnode.right,ans)
        order(root,ans)
        return sum(ans)
