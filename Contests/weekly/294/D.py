class Solution:
    def totalStrength(self, s: List[int]) -> int:
        ans = 0
        MOD = int(1e9+7)
        n = len(s)
        left,right = [-1] * n, [n] * n
        stack = []
        for i,v in enumerate(s):
            while stack and s[stack[-1]] >= v:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        stack2 = []
        for i in range(n-1,-1,-1):
            while stack2 and s[stack2[-1]] > s[i]:
                stack2.pop()
            if stack2:
                right[i] = stack2[-1]
            stack2.append(i)
        '''
        假设我们知道以i为最小值的左右区间为L到R
        s[k]表示k的前缀和
        \sum_{r=i+1}^{R+1}\sum_{l=L}^{i} (s[r]-s[l])
        '''
        f1 = accumulate(s,initial=0)
        f2 = list(accumulate(f1,initial=0))
        for i,v in enumerate(s):
            L,R = left[i] + 1, right[i] - 1
            t = (i-L+1) * (f2[R+2]-f2[i+1]) - ((R-i+1)*(f2[i+1]-f2[L]))
            ans += v * t 
        return ans % MOD 
        
        