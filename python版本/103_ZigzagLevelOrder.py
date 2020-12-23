# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        基本思路是层序遍历，使用一个flag参数记录当前层是奇数层还是偶数层
        偶数层则将存储val的临时数组进行反转后加入ans数组
        '''
        if root is None:
            return []
        ans = []
        queue = [root]
        flag = 0
        while queue:
            temp = []
            next_level = []
            for node in queue:
                temp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            #ans.append(temp)
            queue = next_level
            if flag % 2 == 0:
                ans.append(temp)
            else:
                temp.reverse()
                ans.append(temp)
            flag += 1
        return ans
