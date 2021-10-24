class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        '''
        dp[i]表示为第i门课完成的时间
        '''
        import heapq 
        c1 = collections.defaultdict(list)
        deg = [0] * n
        for x,y in relations:
            c1[x-1].append(y-1)
            deg[y-1] += 1
        q = []
        for i in range(n):
            if deg[i] == 0:
                q.append([time[i],i])
        q.sort()
        while q:
            t,idx = heapq.heappop(q)
            for nxt in c1[idx]:
                deg[nxt] -= 1
                if deg[nxt] == 0:
                    heapq.heappush(q,[t+time[nxt],nxt])
        return t 
        
            