class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ans = 0
        m,n = len(grid), len(grid[0])
        def dfs(x,y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 
            if grid[x][y] == "0":
                return 
            else:
                grid[x][y] = "0"
                for dx,dy in directions:
                    dfs(x+dx, y+dy)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)
        return ans 