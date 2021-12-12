class Solution:
    def goodDaysToRobBank(self, s: List[int], t: int) -> List[int]:
        n = len(s)
        if n < t:
            return []
        dp1 = [1] * n 
        dp2 = [1] * n
        for i in range(n-1):
            if s[i+1] <= s[i]:
                dp1[i+1] = dp1[i] + 1
        #print(dp1)
        
        for j in range(n-1,0,-1):
            if s[j-1] <= s[j]:
                dp2[j-1] = dp2[j] + 1
        #print(dp2)
        ans = []
        for k in range(t,n-t):
            if dp1[k] >= t+1 and dp2[k] >= t+1:
                ans.append(k)
        return ans 