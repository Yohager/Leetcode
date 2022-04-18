class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        if n <= k:
            return s 
        # ans = ''
        while len(s) > k:
            n = len(s)
            ans = ''
            for i in range(0,n,k):
                cur = list(map(int,list(s[i:min(i+k,n)])))
                ans += str(sum(cur))
            s = ans
        return ans 
            