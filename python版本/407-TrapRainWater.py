class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n, ans = len(heightMap), len(heightMap[0]), 0
        visited, dirs, pq = [[False] * n for _ in range(m)], [(0,1),(1,0),(0,-1),(-1,0)], []
        for i in range(1,n-1):
            heapq.heappush(pq,(heightMap[0][i], 0, i))
            heapq.heappush(pq,(heightMap[m-1][i], m-1, i))
        for i in range(1,m-1):
            heapq.heappush(pq, (heightMap[i][0], i, 0))
            heapq.heappush(pq, (heightMap[i][n-1], i, n-1))
        while pq:
            h, x, y = heapq.heappop(pq)
            for dx, dy in dirs:
                nx, ny = x+dx,y+dy
                if 0 < nx < m - 1 and 0 < ny < n - 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    ans += max(0, h - heightMap[nx][ny])
                    heapq.heappush(pq, (max(h, heightMap[nx][ny]), nx, ny))
        return ans