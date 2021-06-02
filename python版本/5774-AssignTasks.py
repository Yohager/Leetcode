class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        ans = []
        pq = [(w,i) for i,w in enumerate(servers)]
        import heapq
        heapq.heapify(pq)
        cur_t = 0
        n = len(servers)
        m = len(tasks)
        busy = []
        def func():
            while busy and busy[0][0] <= cur_t:
                _, idx = heapq.heappop(busy)
                heapq.heappush(pq,(servers[idx],idx))
        for i,t in enumerate(tasks):
            cur_t = max(cur_t,i)
            func()
            if not pq:
                cur_t = busy[0][0]
                func()
            
            _,idx = heapq.heappop(pq)
            ans.append(idx)
            heapq.heappush(busy,(cur_t + t,idx))
        return ans