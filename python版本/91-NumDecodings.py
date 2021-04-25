class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        if s[0] == '0': return 0
        n = len(s)
        if n == 1:
            return 1
        s = ' ' + s
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1,n+1):
            a = ord(s[i]) - ord('0')
            b = (ord(s[i-1])-ord('0')) * 10 +ord(s[i])-ord('0')
            if 1 <= a <= 9:
                dp[i] = dp[i-1]
            if 10 <= b <= 26:
                dp[i] += dp[i-2]
        return dp[n]