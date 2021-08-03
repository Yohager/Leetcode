# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]: 
        g = {}
        def func(node1):
            if node1.left:
                g[node1.left.val] = node1
                func(node1.left)
            if node1.right:
                g[node1.right.val] = node1 
                func(node1.right)
        res = []
        def dfs(root,node,k):
            #需要记录上一个节点是谁
            if k==0:
                res.append(root.val)
                return 
            if root.left and root.left!=node:#左
                dfs(root.left,root,k-1)
            if root.right and root.right!=node:#右
                dfs(root.right,root,k-1)
            if root.val in g and g[root.val]!=node:#父亲
                dfs(g[root.val],root,k-1)
        
        func(root)
        dfs(target,None,k)
        return res