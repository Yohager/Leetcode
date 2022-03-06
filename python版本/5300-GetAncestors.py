class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def bfs(node):
            q = deque([node])
            vis = set()
            while q:
                cur = q.popleft()
                vis.add(cur)
                for x in d[cur]:
                    if x not in vis:
                        q.append(x)
            vis.remove(node)
            return sorted(list(vis))
        d = defaultdict(list)
        for x,y in edges:
            d[y].append(x)
        ans = [[] for _ in range(n)]
        for i in range(n):
            if i not in d.keys():
                continue 
            else:
                ans[i] = bfs(i)
        return ans 
            