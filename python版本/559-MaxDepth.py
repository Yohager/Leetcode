"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # def dfs(node):
        #     if not node:
        #         return 
        #     depth = 0
        #     for c in node.children:
        #         depth = max(depth, dfs(c))
        #     return depth + 1
        # return dfs(root) if root else 0
        def bfs(node):
            if not node:
                return 0 
            if not node.children:
                return 1 
            q = deque()
            q.append(node)
            res = 0 
            while q:
                cnt = len(q)
                res += 1
                while cnt > 0:
                    tmp = q.popleft()
                    if tmp.children:
                        for c in tmp.children:
                            q.append(c)
                    cnt -= 1
            return res 
        return bfs(root)
