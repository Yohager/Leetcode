class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        '''
        定义状态：dp[i][j]表示到第i行的第j个状态
        dp[i][j] = arr[i][j] + min(dp[i-1][j'])(这里的j'表示遍历除了j列的其他所有位置的最小值)
        '''
        m,n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for idx,x in enumerate(grid[0]):
            dp[0][idx] = x
        for i in range(1,m):
            for j in range(n):
                dp[i][j] = grid[i][j] + min([dp[i-1][k] for k in range(n) if k != j])
        return min(dp[-1])