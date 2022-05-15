class Solution:
    def largestCombination(self, c: List[int]) -> int:
        n = len(c)
        ans = 0
        for i in range(31):
            cnt = 0
            for v in c:
                if v & (1 << i):
                    cnt += 1
            ans = max(ans,cnt)
        return ans