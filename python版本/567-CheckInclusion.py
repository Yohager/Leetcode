class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        n1 = len(s1)
        n2 = len(s2)
        c1 = collections.Counter(s1)
        c2 = collections.Counter()
        l,r = 0,0
        while r < n2:
            c2[s2[r]] += 1
            if c1 == c2:
                return True
            r += 1
            if r-l+1 > n1:
                c2[s2[l]] -= 1
                if c2[s2[l]] == 0:
                    del c2[s2[l]]
                l += 1
        return False

