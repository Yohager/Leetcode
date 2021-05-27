class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(n)]
        #这种情况表示的是只需要打印一个元素
        for elem in range(n):
            dp[elem][elem] = 1
        for i in range(n-2,-1,-1):
            #dp[i][j]表示的是s[i,j]这一段字符串的最少的打印次数
            for j in range(i+1,n):
                dp[i][j] = 1 + dp[i+1][j] #这里将i单独打印
                for k in range(i+1,j):
                    if s[i] == s[k]:
                        #此时将i放到[i+1,k]中一起打印
                        dp[i][j] = min(dp[i][j],dp[i+1][k]+dp[k+1][j])
                if s[i] == s[j]:
                    #此时i直接放进[i,j]里面打印即可
                    dp[i][j] = min(dp[i][j], dp[i+1][j])
        return dp[0][-1]
