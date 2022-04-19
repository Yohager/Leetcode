class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        directs = [(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(i,j):
            maxval = 0
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0 
            tmp = grid[i][j]
            grid[i][j] = 0
            for dx,dy in directs:
                maxval = max(maxval,dfs(i+dx,j+dy))
            grid[i][j] = tmp 
            return maxval + tmp 
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans,dfs(i,j))
        return ans