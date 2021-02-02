class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        n = len(s)
        l,r = 0,0
        counter = Counter()
        ans = 0
        while r < n:
            counter[s[r]] += 1
            while r-l+1 - counter.most_common(1)[0][1] > k:
                counter[s[l]] -= 1
                l += 1
            ans = max(ans,r-l+1)
            r += 1
        return ans