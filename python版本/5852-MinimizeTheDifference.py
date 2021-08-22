class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        MAXN = 70
        MAXV = MAXN * MAXN + 1 
        n = len(mat)
        m = len(mat[0])
        dp = [[False]*MAXV for _ in range(MAXN)]
        for x in mat[0]:
            dp[0][x] = True
        for i in range(1,n):
            flag = False
            for j in range(MAXV):
                if flag and j > 2*target:
                    break 
                if not dp[i-1][j]:
                    continue
                for k in range(m):
                    if j + mat[i][k] >= MAXV:
                        continue
                    dp[i][j+mat[i][k]] = True
                    flag = True 
        ans = float('inf')
        for idx in range(MAXV):
            if dp[n-1][idx]:
                ans = min(ans,abs(target-idx))
        return ans