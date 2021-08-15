'''
方法1：深度优先搜索，会超时
class Solution:
    @lru_cache
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        cnt = 0
        if maxMove < 0:
            return cnt 
        if startRow < 0 or startRow >= m or startColumn < 0 or startColumn >= n:
            return 1
        for dx,dy in [(startRow-1,startColumn),(startRow+1,startColumn),(startRow,startColumn-1),(startRow,startColumn+1)]:
            cnt = (cnt + self.findPaths(m,n,maxMove-1,dx,dy)) % 1000000007
        return cnt
'''
class Solution:
    def findPaths(self, m: int, n: int, k: int, i: int, j: int) -> int:
        '''
        dp[i][j][k]表示的是从(i,j)位置移动k步的出界的路径数量
        很显然这个dp的转移方程为：
        dp[i][j][k] = dp[i-1][j][k-1] + dp[i+1][j][k-1] + dp[i][j-1][k-1] + dp[i][j+1][k-1]
        '''
        MOD = 1e9+7
        if k <= 0:
            return 0 
        dp = [[[0]*(k+1) for _ in range(n)] for _ in range(m)]
        dirs = [(0,-1),(0,1),(-1,0),(1,0)]
        for idx in range(1,k+1):
            for x in range(m):
                for y in range(n):
                    for dir in dirs:
                        nx,ny = x+dir[0], y+dir[1]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            dp[x][y][idx] += 1
                        else:
                            dp[x][y][idx] = (dp[x][y][idx] + dp[nx][ny][idx-1]) % MOD 
        return dp[i][j][k]