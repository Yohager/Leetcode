# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root: return []
        queue = [root]
        flag = 0
        while queue:
            temp = []
            n = len(queue)
            for i in range(n):
                node = queue[0]
                queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if flag % 2 == 0:
                ans.append(temp)
            else:
                temp.reverse()
                ans.append(temp)
            flag += 1
        return ans
