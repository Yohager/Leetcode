class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        d = collections.defaultdict(set)
        for x,y in graph:
            d[x].add(y)
        q = deque([start])
        vis = [False] * n 
        while q:
            cur = q.popleft()
            vis[cur] = True 
            for x in d[cur]:
                if not vis[x]:
                    q.append(x)
        return vis[target]