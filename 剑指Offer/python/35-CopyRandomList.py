"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def dfs(head):
            if not head: return None
            if head in visited:
                return visited[head]
            
            tmp = Node(head.val, None, None)
            visited[head] = tmp
            tmp.next = dfs(head.next)
            tmp.random = dfs(head.random)
            return tmp
        visited = {}
        return dfs(head)