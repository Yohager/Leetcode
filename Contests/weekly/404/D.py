class Solution:
    
    # compute the diameter of a tree
    def calc(self, edges):
        g = [[] for _ in range(len(edges) + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        ans = 0
        def dfs(node, pre):
            nonlocal ans 
            max_len = 0
            for y in g[node]:
                if y != pre:
                    sub_len = dfs(y, node) + 1
                    ans = max(ans, max_len + sub_len)
                    max_len = max(max_len, sub_len)
            return max_len
        dfs(0, -1)
        return ans 
    
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        d1 = self.calc(edges1)
        d2 = self.calc(edges2)
        return max((d1 + 1) // 2 + (d2 + 1) // 2 + 1, d1, d2)
        
        
