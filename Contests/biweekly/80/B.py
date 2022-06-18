class Solution:
    def successfulPairs(self, s: List[int], p: List[int], t: int) -> List[int]:
        ans = []
        p.sort()
        n = len(p)
        for ss in s:
            tt = t // ss if t % ss == 0 else t // ss + 1
            idx = bisect.bisect_left(p,tt)
            ans.append(n - idx)
        return ans 