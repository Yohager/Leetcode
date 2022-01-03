class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        rg = defaultdict(set)
        deg = [0] * n 
        for x,y in enumerate(favorite):
            rg[y].add(x)
            deg[y] += 1
        
        q = deque(i for i,d in enumerate(deg) if d == 0) #将所有入读为0的点加进来
        while q:
            cur = q.popleft()
            tar = favorite[cur] #cur只有一条出边
            deg[tar] -= 1
            if deg[tar] == 0:
                q.append(tar)

        def rdfs(node):
            maxdepth = 1
            for x in rg[node]:
                if deg[x] == 0:
                    maxdepth = max(maxdepth, rdfs(x)+1)
            return maxdepth 
        # print(rdfs(0),rdfs(1))
        
        max_cycle, max_chain = 0,0 
        for i,d in enumerate(deg):
            if d <= 0:
                continue 
            deg[i] = -1
            cycle_size = 1
            tar = favorite[i]
            while tar != i:
                deg[tar] = -1 
                cycle_size += 1
                tar = favorite[tar]
            if cycle_size == 2:
                # print(rdfs(0),rdfs(1))
                max_chain += rdfs(i) + rdfs(favorite[i])
            else:
                max_cycle = max(max_cycle,cycle_size)
        # print(max_cycle,max_chain)
        return max(max_cycle,max_chain)