# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def Traversal(node,nums):
            if not node:
                return 
            Traversal(node.left,nums)
            nums.append(node.val)
            Traversal(node.right,nums)
        nums = []
        Traversal(root,nums)
        nums.sort()
        ans = float('inf')
        n = len(nums)
        for i in range(n-1):
            ans = min(ans,nums[i+1]-nums[i])
        return ans