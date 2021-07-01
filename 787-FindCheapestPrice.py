class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # matrix = [[-1 for _ in range(n)] for _ in range(n)]
        # for e in flights:
        #     matrix[e[0]][e[1]] = e[2]
        # #赋权图
        # self.res = float('inf')
        # visited = [False] * n 
        # visited[src] == True 
        # def dfs(cur,nums,steps,visit):
        #     if cur == dst: 
        #         self.res = min(self.res,nums)
        #         return 
        #     if steps > k or nums > self.res:
        #         return 
        #     for x in range(n):
        #         if not visit[x] and matrix[cur][x] != -1:
        #             visit[x] = True
        #             dfs(x,nums+matrix[cur][x],steps + 1,visit)
        #             visit[x] = False 
        # dfs(src,0,0,visited)
        # return self.res if self.res != float('inf') else -1
        '''
        试了dfs会超时还是得用dp
        贝尔曼福德算法
        也是用来求最短路径的算法，只是这个算法的时间复杂度高于dijstra算法
        不过对于这个题目来说刚好适合，因为迭代的次数刚好就是允许走过的最长的边数
        '''
        dist = [float('inf')] * n 
        dist[src] = 0 
        #迭代k+1次
        for i in range(k+1):
            dist_old = dist[:]
            for x,y,z in flights:
                dist[y] = min(dist[y], dist_old[x] + z)
        return dist[dst] if dist[dst] != float('inf') else -1
