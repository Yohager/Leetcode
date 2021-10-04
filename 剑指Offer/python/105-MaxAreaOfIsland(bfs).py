class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directs = {(0,1),(0,-1),(1,0),(-1,0)}
        ans = 0
        
        def bfs(i,j):
            q = deque()
            q.append((i,j))
            grid[i][j] = -1
            cnt = 1
            while q:
                ci,cj = q.popleft()
                #grid[ci][cj] = -1
                for dx,dy in directs:
                    if ci+dx >= 0 and ci+dx < m and cj+dy >= 0 and cj+dy < n and grid[ci+dx][cj+dy] == 1:
                        cnt += 1
                        q.append((ci+dx,cj+dy))
                        grid[ci+dx][cj+dy] = -1
                        
            return cnt 
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    ans = max(ans,bfs(x,y))
        return ans 
                    
