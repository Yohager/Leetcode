class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        g = defaultdict(set)
        n = len(arr)
        tars = []
        for i in range(n):
            if arr[i] == 0:
                tars.append(i)
            if 0 <= i+arr[i] < n:
                g[i].add(i+arr[i])
            if 0 <= i-arr[i] < n:
                g[i].add(i-arr[i])
        #g表示图
        q = deque([start])
        vis = [False] * n 
        vis[start] = True 
        while q:
            cur = q.popleft()
            vis[cur] = True 
            for x in g[cur]:
                if not vis[x]:
                    q.append(x)
        for t in tars:
            if vis[t]:
                return True 
        return False 