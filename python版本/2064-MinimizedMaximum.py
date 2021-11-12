class Solution:
    def minimizedMaximum(self, n: int, q: List[int]) -> int:
        if sum(q) <= n:
            return 1
        def check(val):
            cnt = 0
            for a in q:
                if a % val == 0:
                    cnt += a // val 
                else:
                    cnt += (a // val + 1)
            if cnt > n:
                #太小了
                return 1
            else:
                return -1
        total = sum(q)
        l,r = total // n, max(q)
        while l < r:
            m = (l+r) // 2
            if check(m) == 1:
                l = m + 1
            else:
                r = m - 1 
        if check(l) == 1 and check(l+1) == -1:
            return l + 1
        else:
            return l
            