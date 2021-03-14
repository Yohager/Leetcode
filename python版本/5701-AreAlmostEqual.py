class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        from collections import Counter
        c1 = Counter(s1)
        c2 = Counter(s2)
        if c1 != c2:
            return False
        n = len(s1)
        cnt = 0
        for i in range(n):
            if s1[i] != s2[i]:
                cnt += 1
        if cnt > 2:
            return False
        return True