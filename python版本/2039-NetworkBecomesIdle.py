class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        g = defaultdict(set)
        for x,y in edges:
            g[x].add(y)
            g[y].add(x)

        q = deque([0])
        d = [-1 for _ in range(n)]
        vis = [False] * n
        vis[0] = True 
        dist = 0
        while q:
            l = len(q)
            for _ in range(l):
                cur = q.popleft()
                d[cur] = dist 
                for y in g[cur]:
                    if not vis[y]:
                        q.append(y)
                        vis[y] = True
            dist += 1
        res = 0
        for i in range(1,n):
            time = patience[i] * ((2*d[i]-1)//patience[i]) + 2*d[i] + 1
            res = max(res,time)
        return res 
        