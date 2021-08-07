class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        ans = []
        out = {}
        reverse_g = [[] for i in range(n)]
        #存放所有的终止节点
        end_points = set()
        for i in range(n):
            out[i] = len(graph[i])
            if out[i] == 0:
                end_points.add(i)
            for x in graph[i]:
                reverse_g[x].append(i)
            
        while end_points:
            tmp = end_points.pop()
            ans.append(tmp)
            for k in reverse_g[tmp]:
                out[k] -= 1
                if out[k] == 0:
                    end_points.add(k)
        return sorted(ans)

