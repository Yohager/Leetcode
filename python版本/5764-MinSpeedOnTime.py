class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if sum(dist) <= hour:
            return 1
        if len(dist)-1 > hour:
            return -1
        #出现hour的大小刚刚好比len(dist)大了不超过1      
        n = len(dist)
        l = 1
        r = 10 ** 7
        #判断是否成立
        def func(d,s):
            cnt = 0
            for i in range(len(d)-1):
                cnt += math.ceil(d[i]/s)
            cnt += d[-1]/s
            return cnt
        while l < r:
            mid = (l+r) // 2
            if func(dist,mid) <= hour:
                r = mid
            else:
                l = mid + 1
        return l 
        
        
        