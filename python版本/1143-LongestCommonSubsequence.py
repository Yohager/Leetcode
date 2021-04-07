class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        二维的dp传入的参数是t1和t2的idx
        dp[i][j] = max(dp[i-1][j-1])
        '''
        n1 = len(text1)+1
        n2 = len(text2)+1
        dp = [[0 for _ in range(n2)] for _ in range(n1)]
        for i in range(1,n1):
            for j in range(1,n2):
                if text1[i-1] == text2[j-1]:
                    #此时匹配到了一个字符
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    #此时未匹配上
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return dp[-1][-1]
