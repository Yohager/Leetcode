class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        t = []
        for i,j in enumerate(tasks):
            t.append([j[0],j[1],i])
        t.sort(key=lambda x:(x[0],x[1],x[2]))
        #print(t)
        cur = t[0][0]
        n = len(tasks)
        import heapq
        q = []
        ans = []
        idx = 0
        while len(ans) != n:
            while idx < n and t[idx][0] <= cur:
                tmp = t[idx]
                heappush(q,[tmp[1],tmp[2],tmp[0]])
                idx += 1
            if not q:
                cur = t[idx][1]
                continue
            cur_t = heappop(q)
            ans.append(cur_t[1])
            cur += cur_t[0]
        return ans 