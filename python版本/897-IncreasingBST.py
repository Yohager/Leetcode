# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        ans = TreeNode(0)
        arr = []
        def order(node,l):
            if not node:
                return 
            order(node.left,l)
            l.append(node.val)
            order(node.right,l)
        order(root,arr)
        ans.val = arr[0]
        q = ans
        for i in range(1,len(arr)):
            tmp = TreeNode(arr[i])
            q.right = tmp 
            q = q.right
        return ans 