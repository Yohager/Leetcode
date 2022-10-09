class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = int(1e9) + 7
        m, n = len(grid), len(grid[0])
        ans = 0
        @cache
        def dfs(i, j, v):
            if i < 0 or j < 0:
                return 0
            v = (v + grid[i][j]) % k 
            if i == j == 0:
                return v == 0
            return (dfs(i-1, j, v) + dfs(i, j - 1, v)) % MOD 
        ans = dfs(m-1, n-1, 0)
        dfs.cache_clear()
        return int(ans)