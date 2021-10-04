class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directs = {(0,1),(0,-1),(1,0),(-1,0)}
        ans = 0
        
        @lru_cache(None)
        def dfs(x,y):
            grid[x][y] = -1
            nonlocal ans
            cnt = 1
            for dx,dy in directs:
                if (x+dx) >= 0 and (x+dx) < m and (y+dy) >= 0 and (y+dy) < n and grid[x+dx][y+dy] == 1:
                    cnt += dfs(x+dx,y+dy)
                
            ans = max(ans,cnt)
            return cnt 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
        return ans 