class Solution:
    def minimumTime(self, s: str) -> int:
        ans = -float('inf')
        n = len(s)
        cur = 0
        for i in range(n):
            tmp = 1 if s[i] == '0' else -1 
            cur += tmp 
            if cur < 0:
                cur = 0
            ans = max(ans, cur)
        # print(ans)
        return n - ans 