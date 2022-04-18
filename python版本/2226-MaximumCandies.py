class Solution:
    def maximumCandies(self, c: List[int], k: int) -> int:
        def check(x):
            cnt = 0
            for a in c:
                cnt += (a//x)
            return cnt 
        
        def cals(l,r):
            while l < r:
                m = (l+r) // 2 + 1
                if check(m) >= k:
                    # 可以分的数量多于k
                    # 当前选择的值太小了
                    l = m
                else:
                    r = m - 1
            return l
        
        c.sort()
        total = sum(c)
        if total < k:
            return 0
        cur = cals(1,c[-1])
        return cur 
        #print(cur)
        # if check(cur) == k:
        #     return cur 
        # elif check(cur) < k:
        #     return cur - 1
        