from queue import PriorityQueue as pQueue
class DistanceAlg():
    def __init__(self,edges,n):
        #输入的数据为节点的数量，存储边的数组
        self.edges = edges
        self.graph = [[] for _ in range(n)]
    
    def construct_matrix(self):
        for edge in self.edges:
            self.graph[edge[0]-1].append([edge[1],edge[2]])
            self.graph[edge[1]-1].append([edge[0],edge[2]])
    
    #求解path的过程(不带优化的代码)
    def dij(self,start):
        l = len(self.graph)
        costs = [float('inf') for _ in range (l)]
        #到自己的距离为0
        costs[start-1] = 0
        parents = [-1 for _ in range(l)]
        visited = [False for _ in range(l)]
        #t用于计数考虑是否所有的节点都已经计算过他们的邻居了
        t = 1
        while t < l:
            mincost = float('inf')
            minnode = None
            for i in range(l):
                if not visited[i] and costs[i] < mincost:
                    mincost = costs[i]
                    minnode = i 
            t += 1
            visited[minnode] = True 
            for edge in self.graph[minnode]:
                if not visited[edge[0]-1] and mincost + edge[1] < costs[edge[0]-1]:
                    costs[edge[0]-1] = mincost + edge[1]
                    parents[edge[0]-1] = minnode
        return costs, parents

    #对于dijistra算法的优化
    def dij_opt(self,start):
        l = len(self.graph)
        q = pQueue()
        #进入队列中的元素应该为[cost,v]的形式
        visited = [False for _ in range(l)]
        t = {}
        parents = [-1 for _ in range(l)]
        q.put([0,start,-1])
        while len(t) < n:
            minpath = q.get()
            while visited[minpath[1]-1]:
                minpath = q.get()
            minnode = minpath[1]
            visited[minnode-1] = True
            t[minnode-1] = minpath[0]
            parents[minnode-1] = minpath[2]
            for edge in self.graph[minnode-1]:
                if not visited[edge[0]-1]:
                    q.put([edge[1]+t[minnode-1],edge[0],minnode])
        return t,parents


if __name__ =="__main__":
    n = 5
    edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
    temp = DistanceAlg(edges,n)
    temp.construct_matrix()
    c1,p1 = temp.dij(5)
    c2,p2 = temp.dij_opt(5)
    print(c1,c2)
    print(p1,p2)