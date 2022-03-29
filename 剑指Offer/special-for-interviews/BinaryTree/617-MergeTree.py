'''
合并两个二叉树
递归
输入: 两个根节点
递归出口: 两个节点都不存在则退出 存在一个节点直接返回该节点
递归: 两个左子树递归, 两个右子树递归
最后返回第一个树 (我们考虑将第二颗树的值加到第一颗树上)
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None 
        else:
            rootv = preorder.pop(0)
            root_idx = inorder.index(rootv)
            root = TreeNode(inorder[root_idx])
            root.left = self.buildTree(preorder,inorder[:root_idx])
            root.right = self.buildTree(preorder,inorder[root_idx+1:])
            return root 