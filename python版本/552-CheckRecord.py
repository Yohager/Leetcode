class Solution:
    def checkRecord(self, n: int) -> int:
        '''
        如果没有出现A
        dp[i][j]表示第i天以j结尾的情况
        L: 1; P: 0
        如果i天是P那么前一天的任意状态都可以转移过来
        如果i天是L：考虑前一天如果也是L则再前一天只能是P，如果前一天是P则可以任意转移
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-2][0] + dp[i-1][0]

        如果出现有A的情况
        从A出现的位置将区间划分为两部分，这两个部分都满足没有出现A的情况
        总方案数就是左右两边的方案数相乘
        '''
        MOD = 1000000007
        if n == 1: return 3
        dp = [[0,0] for _ in range(n)]
        dp[0][0],dp[0][1] = 1,1
        dp[1][0],dp[1][1] = 2,2
        for i in range(2,n):
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-2][0] + dp[i-1][0]
            dp[i][0] = dp[i][0] % MOD 
            dp[i][1] = dp[i][1] % MOD
        ans = ((dp[n-1][0]+dp[n-1][1]) + (dp[n-2][0]+dp[n-2][1])*2) % MOD 
        for l in range(n-2):
            r = n-3-l #左边区间的长度为l，右边区间的长度为总长度减去一个A的位置
            ans += (dp[l][0]+dp[l][1]) * (dp[r][0]+dp[r][1])
            ans = ans % MOD 
        return ans % MOD