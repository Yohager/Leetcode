class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l,r = 0,0
        ans = 0
        from collections import defaultdict
        c = defaultdict(lambda:0)
        while r < n:
            c[s[r]] += 1
            while c[s[r]] > 1:
                c[s[l]] -= 1
                l += 1
            ans = max(ans,r-l+1)
            r += 1
        return ans