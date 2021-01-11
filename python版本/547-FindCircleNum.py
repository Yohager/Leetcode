class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(matrix,v,i):
            for j in range(len(matrix)):
                if matrix[i][j] == 1 and not v[j]:
                    v[j] = 1
                    dfs(matrix,v,j)       
        ans = 0
        n = len(isConnected)
        visited = [0] * n 
        for i in range(n):
            if not visited[i]:
                dfs(isConnected,visited,i)
                ans += 1
        return ans



            