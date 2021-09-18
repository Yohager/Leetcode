# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        if not root:
            return root 
        def preorder(node):
            nonlocal arr 
            if not node:
                return 
            arr.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        root.left = None 
        tmp = root 
        idx = 1
        while idx < len(arr):
            newnode = TreeNode(arr[idx])
            newnode.left = None 
            tmp.right = newnode
            tmp = tmp.right 
            idx += 1