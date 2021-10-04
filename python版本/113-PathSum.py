# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node,val,tmp):
            #print(tmp)
            nonlocal ans 
            if not node:
                return 
            if not node.left and not node.right:
                if val == node.val:
                    tmp.append(node.val)
                    ans.append(tmp)
                    return 
            dfs(node.left,val-node.val,tmp+[node.val])
            dfs(node.right,val-node.val,tmp+[node.val])
        
        if not root:
            return ans 
        dfs(root,targetSum,[])
        return ans 
