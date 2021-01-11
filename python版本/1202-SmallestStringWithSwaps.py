class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        graph = [[] for _ in range(n)]
        visited = [0] * n
        for i,j in pairs:
            graph[i].append(j)
            graph[j].append(i)
        #print(graph)
        def dfs(res,graph,visited,index):
            for k in graph[index]:
                if not visited[k]:
                    visited[k] = 1
                    res.append(k)
                    dfs(res,graph,visited,k)
        res = list(s)
        for i in range(n):
            if not visited[i]:
                connects = []
                dfs(connects,graph,visited,i)
                indexs = sorted(connects)
                string = sorted(res[j] for j in connects)
                for m,n in zip(indexs,string):
                    res[m] = n 
        return "".join(res)