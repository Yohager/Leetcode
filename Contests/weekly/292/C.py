class Solution:
    def countTexts(self, p: str) -> int:
        MOD = int(1e9+7)
        if not p:
            return 0
        n = len(p)
        
        f = [0] * (n+50)
        f[0],f[1],f[2] = 1,1,2
        for i in range(3,n+1):
            f[i] = (f[i-1]+f[i-2]+f[i-3]) % MOD 
        g = [0] * (n+50)
        g[0],g[1],g[2],g[3] = 1,1,2,4
        for i in range(4,n+1):
            g[i] = (g[i-1]+g[i-2]+g[i-3]+g[i-4]) % MOD 
        ans = 1
        l,r = 0,0
        while l < n and r < n:
            while r < n and p[l] == p[r]:
                r += 1
            if p[l] == '7' or p[l] == '9':
                ans = (ans * g[r-l]) % MOD 
            else:
                ans = (ans * f[r-l]) % MOD 
            l = r 
        return ans % MOD 