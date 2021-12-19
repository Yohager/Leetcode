class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        r = [max(l) for l in grid]
        c = [max([w[i] for w in grid]) for i in range(n)]
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += min(r[i],c[j]) - grid[i][j]
        return ans 