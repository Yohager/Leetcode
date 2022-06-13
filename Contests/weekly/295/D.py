class Solution:
    def minimumObstacles(self, grid) -> int:
       # 0-1 bfs 
        m,n = len(grid), len(grid[0])
        dist = [[inf]* n for _ in range(m)]
        dist[0][0] = 0
        q = deque([(0,0)])
        while q:
            x,y = q.popleft()
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                if 0 <= x+dx < m and 0 <= y+dy < n:
                    g = grid[x][y]
                    if dist[x][y] + g < dist[x+dx][y+dy]:
                        dist[x+dx][y+dy] = dist[x][y] + g
                        if g == 0:
                            q.appendleft((x+dx,y+dy))
                        else:
                            q.append((x+dy,y+dy))
        return dist[-1][-1]