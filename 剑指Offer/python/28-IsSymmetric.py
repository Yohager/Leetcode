# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def compare(tree1,tree2):
            if tree1 == None and tree2 == None:
                return True
            if (tree1 == None and tree2 != None) or (tree1 != None and tree2 == None):
                return False
            if tree1.val != tree2.val:
                return False
            return compare(tree1.left, tree2.right) and compare(tree1.right, tree2.left)
        return compare(root, root)