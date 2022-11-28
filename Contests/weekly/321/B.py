class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        l, r = 0, 0
        while l < m and r < n:
            if s[l] == t[r]:
                r += 1
            l += 1
        return n - r
            
        