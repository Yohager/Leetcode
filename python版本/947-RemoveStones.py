class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        if not stones: return 0
        ans = 0
        n = len(stones)
        graph = collections.defaultdict(list)
        for i,(x1,y1) in enumerate(stones):
            for j,(x2,y2) in enumerate(stones):
                if x1 == x2 or y1 == y2:
                    graph[i].append(j)
        
        def dfs(node,visited,graph):
            visited.add(node)
            for k in graph[node]:
                if k not in visited:
                    dfs(k,visited,graph)
        
        visited = set()
        for node in range(n):
            if node not in visited:
                ans += 1
                dfs(node,visited,graph)
        return n - ans
        
