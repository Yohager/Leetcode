from InitTree import TreeNode 

'''
平衡二叉树是具有以下性质的二叉搜索树
1. 左右子树的高度差绝对值小于等于1
2. 左右子树都是平衡二叉树
'''

class AVL:
    def __init__(self,nums) -> None:
        self.nums = nums 
    
    def 