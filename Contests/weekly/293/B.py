class Solution:
    def maxConsecutive(self, b: int, t: int, s: List[int]) -> int:
        s.sort()
        ans = 0
        n = len(s)
        start = s[0] - b
        end = t - s[-1]
        pre = s[0]
        ans = max(ans,start,end)
        i = 1
        while i < n:
            cur = s[i]
            if cur - pre - 1 > ans:
                ans = cur - pre - 1
            pre = cur 
            i += 1
        return ans 