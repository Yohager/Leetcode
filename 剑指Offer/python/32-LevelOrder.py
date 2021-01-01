# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        queue = []
        if root != None:
            queue.append(root)
        ans = []
        while queue != []:
            if queue[0] != None:
                ans.append(queue[0].val)
                queue.append(queue[0].left)
                queue.append(queue[0].right)
            queue.pop(0)
        return ans