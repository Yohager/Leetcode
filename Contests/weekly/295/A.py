class Solution:
    def rearrangeCharacters(self, s: str, t: str) -> int:
        c1 = Counter(s)
        c2 = Counter(t)
        res = float('inf')
        for k in c2:
            res = min(res, c1[k]//c2[k])
        return res 