# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        '''
        第一步定位
        '''
        if B == None: return False
        val = B.val
        temp = A
        pos = []
        queue = [temp]
        while queue != []:
            if queue[0].val == val:
                pos.append(queue[0])
            if queue[0].left != None:
                queue.append(queue[0].left)
            if queue[0].right != None:
                queue.append(queue[0].right)
            queue.pop(0)
        '''
        第二步比较
        '''
        def compare_tree(tree1,tree2):
            if tree2 == None:
                return True
            if tree1 == None:
                return False
            if tree1.val != tree2.val:
                return False
            return compare_tree(tree1.left, tree2.left) and compare_tree(tree1.right, tree2.right)
        for k in pos:
            if compare_tree(k,B):
                return True
        return False

