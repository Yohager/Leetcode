class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(bloomDay,d,m,k):
            cnt = 0
            ans = 0
            for i in bloomDay:
                if i <= d:
                    cnt += 1
                    if cnt >= k:
                        cnt -= k
                        m -= 1
                else:
                    cnt = 0
            return m <= 0
                    
        total = m * k 
        n = len(bloomDay)
        if total > n:
            return -1 
        #最早不会早于第一个值，最晚不会晚于最后一个值
        l,r = min(bloomDay), max(bloomDay)
        while l <= r:
            mid = (l + r) // 2
            if check(bloomDay,mid,m,k):
                r = mid - 1
            else:
                l = mid + 1
            
        return l