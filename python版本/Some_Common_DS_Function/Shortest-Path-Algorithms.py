'''
一些最短路径算法的汇总
'''
from heapq import heapify, heappop


def dijkstra_basic(edges,n,start):
    '''
    这是最朴素的dijkstra算法
    数据量较小的稠密图 n^2复杂度
    不允许边权重为负数
    '''
    adjs = [[float('inf') for _ in range(n)] for _ in range(n)]
    #将顶点的序号归一化到从0开始
    for x,y,c in edges:
        x -= 1
        y -= 1
        adjs[x][y] = c
    src = start - 1
    dist = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    dist[src] = 0
    for _ in range(n-1):
        #每一次循环去找还未访问过的节点以及那些距离src点最近的点
        min_dist = float('inf')
        min_node = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_node = i
                min_dist = dist[i]
        if min_node == -1: 
            break 
        #标记新访问到的节点
        visited[min_node] = True 
        #同时需要更新其他的可能经过当前min_node的点而改变的更短的路径
        for j in range(n):
            if adjs[min_node][j] < float('inf'):
                if dist[min_node] + adjs[min_node][j] < dist[j]:
                    dist[j] = dist[min_node] + adjs[min_node][j]
        print(dist)
    return dist 


def dijkstra_heap(edges,n,start):
    '''
    使用最小堆维护的最短路径算法
    '''
    import collections
    adj = collections.defaultdict(list)
    for x,y,c in edges:
        x -= 1 
        y -= 1
        adj[x].append((y,c))
    src = start - 1
    dist = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    dist[src] = 0 
    q = []
    import heapq 
    heapq.heapify(q)
    heapq.heappush(q,(0,src))
    while q:
        d,x = heapq.heappop(q)
        if visited[x]:
            continue 
        visited[x] = True 
        for y,c in adj[x]:
            if dist[x] + c < dist[y]:
                dist[y] = dist[x] + c 
                heapq.heappush(q,(dist[y],y))
    return dist 


def spfa(edges,n,start):
    '''
    效率比较高的单源最短路径算法
    '''
    import collections
    adj = collections.defaultdict(list)
    for x,y,c in edges:
        x -= 1 
        y -= 1
        adj[x].append((y,c))
    src = start - 1
    dist = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    q = collections.deque()
    q.append(src)
    dist[src] = 0
    visited[src] = True 
    while q:
        x = q.popleft()
        visited[x] = True 
        for y,c in adj[x]:
            if dist[x] + c < dist[y]:
                dist[y] = dist[x] + c 
                visited[y] = True
                q.append(y)
    return dist 


if __name__ == "__main__":
    edges = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    print(spfa(edges,n,2)) 

        