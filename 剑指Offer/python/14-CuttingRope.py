class Solution:
    def cuttingRope(self, n: int) -> int:
        '''
        尽可能拆分为多个3个求和
        '''
        # if n <= 3:
        #     return n-1
        # else:
        #     quotient = n // 3
        #     if n % 3 == 0:
        #         return 3**quotient
        #     elif n % 3 == 1:
        #         return 3**(quotient-1)*4
        #     elif n % 3 == 2:
        #         return 3**(quotient)*2
        '''
        使用dp算法求解这个问题
        对于正整数n分解的最大乘积可以表示为：dp[n] = max{
            j*(n-j),
            dp[j] * (n-j),
            j * dp[n-j],
            dp[i] * dp[n-j]
        }
        '''
        if n <= 3:
            return n-1
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            tempmax = 0
            for j in range(1,i):
                tmp = max(j*(i-j),dp[j]*(i-j),j*dp[i-j],dp[i]*dp[i-j])
                tempmax = max(tempmax,tmp)
            dp[i] = tempmax
        return dp[-1]
        