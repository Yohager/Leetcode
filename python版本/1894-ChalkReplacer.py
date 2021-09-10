class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        idx = 0
        cur = 0
        sum1 = sum(chalk)
        times = k // sum1 
        k = k - (times*sum1)
        while k>=0:
            cur = idx % n 
            k -= chalk[cur]
            idx += 1
            #print(cur,k)
        return cur