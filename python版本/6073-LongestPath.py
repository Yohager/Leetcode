class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
        
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # if parent == [-1,0,0,0] and s == "aabc":
        #     return 2
        arr = [TreeNode(e) for e in s]
        for i,p in enumerate(parent):
            if p == -1:
                continue 
            arr[p].children.append(arr[i])
        ans = 0
        def dfs(node):
            nonlocal ans 
            if not node.children:
                return 1
            f,s = 0,0
            for c in node.children:
                # if c.val == node.val:
                #     return 
                tmp = dfs(c)
                # print('here',c.val,tmp)
                if c.val != node.val:
                    if tmp > f:
                        f,s = tmp,f
                    elif tmp > s:
                        s = tmp 
            ans = max(ans,f+s)
            return f + 1
                
        dfs(arr[0])
        # print(ans)
        return ans + 1
        