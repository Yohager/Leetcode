class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        a = sorted(cnt.keys())
        
        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            x = a[i]
            j = i
            while j > 0 and a[j - 1] >= x - 2:
                j -= 1
            return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])
        return dfs(len(a) - 1)
