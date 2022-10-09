class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        # 以中间的值为遍历对象 
        ans = 0
        dirs = [(-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        m, n = len(grid), len(grid[0])
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                cur = grid[i][j]
                for dx, dy in dirs:
                    cur += grid[i+dx][j+dy]
                ans = max(ans, cur)
        return ans 