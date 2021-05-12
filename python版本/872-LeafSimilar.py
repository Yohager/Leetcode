# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leaves(root,arr):
            if not root:
                return 
            if not root.left and not root.right:
                arr.append(root.val)
            leaves(root.left,arr)
            leaves(root.right,arr)
        
        list1 = []
        list2 = []
        leaves(root1,list1)
        leaves(root2,list2)
        return list1 == list2
