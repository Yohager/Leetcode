# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], sv: int, dv: int) -> str:
        #求最近的祖先
        sp = ''
        dp = ''
        def lowest(node,s,d):
            if not node:
                return 
            if node.val == s or node.val == d:
                return node 
            l = lowest(node.left,s,d)
            r = lowest(node.right,s,d)
            if l and r:
                return node 
            elif l:
                return l 
            elif r:
                return r 
            else:
                return 
        
        def path(node,t,p): 
            if not node:
                return False
            p.append(node)
            if node.val == t:
                return True 
            if path(node.left,t,p):
                return True
            if path(node.right,t,p):
                return True
            p.pop()
            return False
        
        low = lowest(root,sv,dv)
        lp = []
        rp = []
        path(low,sv,lp)
        path(low,dv,rp)
        ans = ''
        for i in range(1,len(lp)):
            if lp[i-1].left and lp[i-1].left.val == lp[i].val:
                ans += 'U'
            elif lp[i-1].right and lp[i-1].right.val == lp[i].val:
                ans += 'U'
        for j in range(1,len(rp)):
            if rp[j-1].left and rp[j-1].left.val == rp[j].val:
                ans += 'L'
            elif rp[j-1].right and rp[j-1].right.val == rp[j].val:
                ans += 'R'            
        return ans 
        