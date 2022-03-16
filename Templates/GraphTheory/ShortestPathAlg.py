'''
一些计算最短路径的模板
有向图 无权 无自环 无重边
'''
import collections
from dis import dis
import heapq 


class SPA:
    def __init__(self,edges,n) -> None:
        self.edges = edges 
        self.cnt = n 
        self.graph = collections.defaultdict(set)

    def Initialize(self):
        for x,y in self.edges:
            self.graph[x].add(y)
    
    def Dijistra(self,s):
        # 计算从s到图中各个节点的路径的长度
        dist = [float('inf')] * self.cnt
        dist[s] = 0 
        vis = [False] * self.cnt 
        num = 0
        for _ in range(self.cnt):
            #print(dist)
            cur = float('inf') # 记录当前的最小cost
            node = -1 
            for i in range(self.cnt):
                if not vis[i] and dist[i] < cur:
                    cur = dist[i]
                    node = i 
            # print(cur,node)   
            if node == -1: 
                break 
            vis[node] = True 
            # print(self.graph)
            for x in self.graph[node]:
                if cur + 1 < dist[x]:
                    dist[x] = cur + 1
        return dist
    
    def DijistraHeap(self,s):
        dist = [float('inf')] * n 
        vis = [False] * n 
        dist[s] = 0
        q = []
        heapq.heapify(q)
        heapq.heappush(q,(dist[s],s))
        while q:
            d,x = heapq.heappop(q)
            if vis[x]:
                continue 
            vis[x] = True 
            for y in self.graph[x]:
                if dist[x] + 1 < dist[y]:
                    dist[y] = dist[x] + 1
                    heapq.heappush(q,(dist[y],y))
        return dist 
    
    def SPFA(self,s):
        # 单源最短路算法
        dist = [float('inf')] * n 
        vis = [False] * n 
        q = collections.deque([])
        q.append(s)
        dist[s], vis[s] = 0, True 
        # shortest_path_edges = []
        while q:
            x = q.popleft()
            vis[x] = True 
            # tmp_x = []
            for y in self.graph[x]:
                if dist[x] + 1 < dist[y]:
                    # tmp_x.append([x,y])
                    dist[y] = dist[x] + 1
                    vis[y] = True 
                    q.append(y)
            # shortest_path_edges.append(tmp_x)
            # print(tmp_x)
        return dist        




if __name__ == "__main__":
    n = 5
    edges = [[0,1],[0,2],[2,3],[3,4]]
    s = 0
    spa1 = SPA(edges,n)
    spa1.Initialize()
    print(spa1.Dijistra(s))
    print(spa1.DijistraHeap(s))
    print(spa1.SPFA(s))

