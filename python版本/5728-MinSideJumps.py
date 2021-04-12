class Solution:
    def minSideJumps(self, o: List[int]) -> int:
        #特殊情况是有一条跑道没有障碍
        c = collections.Counter(o)
        if c[2] == 0:
            return 0
        if c[1] == 0 or c[3] == 0:
            return 1
        n = len(o)
        dp = [[n for _ in range(n)] for _ in range(3)]
        dp[0][-1] = 0
        dp[1][-1] = 0
        dp[2][-1] = 0
        #print(dp)
        for x in range(1,n-1):
            if o[x] != 0:
                dp[o[x]-1][x] = float('inf')
        #先处理有障碍的地方
        #print(dp)
        for i in range(n-2,-1,-1):
            if dp[1][i] != float('inf'):
                dp[1][i] = min(dp[1][i+1],1+dp[0][i],1+dp[2][i])
            if dp[2][i] != float('inf'):
                dp[2][i] = min(dp[2][i+1],1+dp[0][i],1+dp[1][i])
            if dp[0][i] != float('inf'):
                dp[0][i] = min(dp[0][i+1],1+dp[1][i],1+dp[2][i])
            if dp[1][i] != float('inf'):
                dp[1][i] = min(dp[1][i+1],1+dp[0][i],1+dp[2][i])
            if dp[2][i] != float('inf'):
                dp[2][i] = min(dp[2][i+1],1+dp[0][i],1+dp[1][i])
            if dp[0][i] != float('inf'):
                dp[0][i] = min(dp[0][i+1],1+dp[1][i],1+dp[2][i])
        #print(dp)
        return dp[1][0]