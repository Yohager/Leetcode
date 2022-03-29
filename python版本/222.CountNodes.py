# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 
        lh = 0
        l = root 
        while l:
            l = l.left
            lh += 1
        lb,rb = int(2**(lh-1)), int(2**(lh)-1)
        while lb <= rb:
            m = lb + (rb - lb) // 2
            path = int(2**(lh-2))
            node = root 
            while node and path > 0:
                if m & path:
                    node = node.right 
                else:
                    node = node.left 
                path //= 2
            if node:
                lb = m + 1
            else:
                rb = m - 1
        return rb