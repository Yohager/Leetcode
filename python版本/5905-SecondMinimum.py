def dijkstra(edges,start):
    n = len(edges)
    vis = [False] * n
    w = [float('inf')] * n
    paths = [None] * n
    q = []
    w[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        x,y = heapq.heappop(q)
        vis[y] = True 
        for v,c in edges[y]:
            if not vis[v]:
                f = x + c 
                if f < w[v]:
                    w[v] = f
                    paths[v] = y
                    heapq.heappush(q,(f,v))
    return paths,w 


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        r = time % change
        cycle_len = time + r 
        w_edges = [[] for _ in range(n)]
        c = collections.defaultdict(set)
        for x,y in edges:
            x -= 1
            y -= 1
            w_edges[x].append([y,1])
            w_edges[y].append([x,1])
            c[x].add(y)
            c[y].add(x)
        
        paths, w = dijkstra(w_edges,0)
        minval = w[-1]
        minpath = [n-1]
        while minpath[-1] != 0:
            minpath.append(paths[minpath[-1]])
        flag = False 
        for x in minpath[:-1]:
            for prev in c[x]:
                if w[x] == w[prev]:
                    flag = True 
        if flag:
            minval += 1 
        else:
            minval += 2
            
        cur = 0
        for _ in range(minval-1):
            cur += time
            if change <= cur % (change*2) < change*2:
                cur += change*2 - cur%(change*2)
        cur += time 
        return cur
            
        