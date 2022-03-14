class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m,n = len(grid), len(grid[0])
        maxv = 0 
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            v = 1
            grid[i][j] = 0
            for dx,dy in dirs:
                v += dfs(i+dx,j+dy)
            return v 
        for i in range(m):
            for j in range(n):
                maxv = max(maxv,dfs(i,j))
        return maxv 