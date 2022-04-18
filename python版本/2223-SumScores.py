class Solution:
    def sumScores(self, s: str) -> int:
        MOD = 10**9+7
        base = 31
        ans = 0
        n = len(s)
        prefix = [0] * (n+1)
        mul = [1] * (n+1)
        for i in range(1,n+1):
            prefix[i] = (prefix[i-1]*base + ord(s[i-1])-ord('a')+1) % MOD 
            mul[i] = mul[i-1] * base % MOD 
        for i in range(n):
            if s[i] != s[0]:
                continue
            l,r = 0,n-i
            while l < r:
                m = (l+r+1)//2
                hv = (prefix[i+m]-prefix[i]*mul[m] % MOD + MOD) % MOD 
                if hv == prefix[m]:
                    l = m 
                else:
                    r = m - 1
            # print(l)
            ans += l
        return ans 