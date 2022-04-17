class Solution:
    def waysToBuyPensPencils(self, t: int, c1: int, c2: int) -> int:
        if t < c1 and t < c2:
            return 1 
        ans = 0
        m = t // c1 # 最多买多少个c1
        for i in range(m+1):
            cur = t - c1*i 
            if cur == 0:
                ans += 1
            else:
                ans += (cur // c2) + 1
        return ans 
        