class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        ans = ''
        rounds = n // (2*k)
        for i in range(rounds):
            ans += s[2*k*i:2*k*(i+1)][:k][::-1]
            ans += s[2*k*i:2*k*(i+1)][k:]
        if n - (2*rounds*k) < k:
            ans += s[2*rounds*k:][::-1]
        else:
            ans += s[2*rounds*k:(2*rounds+1)*k][::-1]
            ans += s[(2*rounds+1)*k:]
        return ans 