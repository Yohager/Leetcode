class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topsort(items,indegree,neighbors):
            queue = collections.deque()
            res = []
            for i in items:
                if not indegree[i]:
                    queue.append(i)
            
            if not queue: return []
            while queue:
                cur = queue.popleft()
                res.append(cur)

                for j in neighbors[cur]:
                    indegree[j] -= 1
                    if not indegree[j]:
                        queue.append(j)
            return res
        
        #两层拓扑排序
        GroupNum = m
        for i in range(n):
            if group[i] == -1:
                group[i] = GroupNum
                GroupNum += 1
        
        t = [0] * n
        g = [0] * GroupNum
        t_n = [[] for _ in range(n)]
        g_n = [[] for _ in range(GroupNum)]
        g_t = [[] for _ in range(GroupNum)]

        for j in range(n):
            g_t[group[j]].append(j)
            for k in beforeItems[j]:
                #非一个小组的tasks
                if group[k] != group[j]:
                    g[group[j]] += 1
                    g_n[group[k]].append(group[j])
                else:
                    t[j] += 1
                    t_n[k].append(j)
        ans = []
        group_queue = topsort([i for i in range(GroupNum)],g,g_n)
        if len(group_queue) != GroupNum:
            return []
        for g in group_queue:
            t_q = topsort(g_t[g],t,t_n)
            if len(t_q) != len(g_t[g]):
                return []
            ans += t_q
        
        return ans







