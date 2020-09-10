# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
问题的思路就是：
首先根据先序遍历找到根节点
然后根据中序遍历得到根节点的位置，根据根节点的位置将中序遍历分解
分解为子问题，递归地在左右子树上分别寻找根节点
'''


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        length = len(preorder)
        if length == 0:
            return None
        root_val = preorder[0]
        index = 0
        #找到root节点在中序遍历中的位置这样方便下面的递归
        for i in range(len(inorder)):
            if inorder[i] == root_val:
                index = i
                break
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:index+1],inorder[:index])
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        return root