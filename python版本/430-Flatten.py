"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        ans = []
        def dfs(node):
            nonlocal ans 
            if not node:
                return 
            ans.append(node.val)
            dfs(node.child)
            #ns.append(node.val)
            dfs(node.next)
        dfs(head)
        res = Node(ans[0],None,None,None)
        tmp = res 
        idx = 1
        n = len(ans)
        last = tmp
        while idx < n:
            newnode = Node(ans[idx],None,None,None)
            tmp.next = newnode
            tmp = newnode
            tmp.prev = last
            last = newnode
            idx += 1
        return res 
