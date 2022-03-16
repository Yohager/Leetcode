from collections import *
from tkinter.tix import Tree
from InitTree import TreeNode 

'''
二叉搜索树
对任意一棵子树都满足:
左子树的所有元素值小于根节点
右子树的所有元素值大于根节点
'''

class BST:
    def __init__(self,nums) -> None:
        self.nums = nums 
        self.tree = None 
    
    def SearchBST(self,root,val):
        if not root or val == root.val:
            return root 
        if val < root.val:
            return self.SearchBST(root.left,val)
        else:
            return self.SearchBST(root.right,val)
        
    def InsertBST(self,root,val):
        if not root:
            return TreeNode(val)
        elif val < root.val:
            root.left = self.InsertBST(root.left,val)
        elif val > root.val:
            root.right = self.InsertBST(root.right,val)
        return root 
    
    def ConstructionBST(self):
        for num in self.nums:
            self.tree = self.InsertBST(self.tree,num)
        
    # 查找二叉搜索树中的最大值和最小值
    def FindBSTMin(self,root):
        if root.left:
            return self.FindBSTMin(root.left)
        else:
            return root 
        
    def FindBSTMax(self,root):
        if root.right:
            return self.FindBSTMax(root.right)
        else:
            return root 
        
    '''
    比较难的一个部分
    在二叉搜索树中删除某个元素
    分情况讨论:
    1. 若无左无右则直接删除
    2. 若有左无右或者有右无左则有的一边替换即可
    3. 既有左又有右则找到右边的最小值使用该节点替换要删除的节点
    '''
    def DeleteBST(self,root,val):
        if not root:
            return None 
        # pos表示val所处的位置
        elif val < root.val:
            root.left = self.DeleteBST(root.left,val)
        elif val > root.val:
            root.right = self.DeleteBST(root.right,val)
        else:
            if root.left and root.right:
                # 左右子树都存在
                # 找到右子树的最小值
                subs = self.FindBSTMin(root.right)
                root.val = subs.val 
                root.right = self.DeleteBST(root.right,subs.val)
            elif not root.left and not root.right:
                # 左右子树都没有
                # print('here')
                root = None 
            elif not root.right:
                # 只有左子树
                root = root.left 
            elif not root.left:
                root = root.right
        return root  

    
    def ShowBST(self,root):
        if not root:
            return 
        self.ShowBST(root.left)
        print(root.val)
        self.ShowBST(root.right)

if __name__ == "__main__":
    arr = [1,4,5,3,6,7]
    NewBST = BST(arr)
    NewBST.ConstructionBST()
    NewBST.ShowBST(NewBST.tree)
    # print(NewBST.tree)
    # print(NewBST.SearchBST(NewBST.tree,7))
    # print(NewBST.SearchBST(NewBST.tree,2))
    # print(NewBST.DeleteBST(NewBST.tree,5))
    # NewBST.ShowBST(NewBST.DeleteBST(NewBST.tree,5))
    NewBST.ShowBST(NewBST.InsertBST(NewBST.tree,2))