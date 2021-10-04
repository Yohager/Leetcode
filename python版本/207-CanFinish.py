class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        # matrix = [[0]*n for _ in range(n)]
        # for x,y in prerequisites:
        #     matrix[x][y] = 1
        # #根据邻接矩阵判定是否存在环路的问题
        d = collections.defaultdict(set)
        for x,y in prerequisites:
            d[y].add(x)
        visited = [0] * n
        flag = False
        res = []
        @lru_cache(None)
        def dfs(root):
            nonlocal flag  
            visited[root] = 1
            for k in d[root]:
                if visited[k] == 1:
                    #存在环
                    flag = True 
                    return 
                elif visited[k] == 0:
                    dfs(k)
                    if flag == True:
                        return 
            visited[root] = 2
            res.append(root)
        for i in range(n):
            if not visited[i] and i not in res:
                dfs(i)
        return True if not flag else False