class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], s1: int, s2: int, dest: int) -> int:
        g = defaultdict(set)
        gre = defaultdict(set)
        for x,y,c in edges:
            g[x].add((y,c))
            gre[y].add((x,c))
        
        def dij_heap(g,s,n):
            vis = [False]*n
            dist = [float('inf')]*n 
            dist[s] = 0
            q = []
            heapq.heapify(q)
            heapq.heappush(q,(0,s))
            while q:
                d,cur = heapq.heappop(q)
                if vis[cur]:
                    continue 
                vis[cur] = True 
                for y,c in g[cur]:
                    if dist[cur]+c < dist[y]:
                        dist[y] = dist[cur] + c
                        heapq.heappush(q,(dist[y],y)) 
            return dist
        ans = float('inf')
        d1 = dij_heap(g,s1,n)
        d2 = dij_heap(g,s2,n)
        dd = dij_heap(gre,dest,n)
        for i in range(n):
            ans = min(ans,d1[i]+d2[i]+dd[i])
        return ans if ans != float('inf') else -1