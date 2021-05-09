class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def backtrace(arr, g, limit):
            if not arr:
                return True 
            v = arr.pop()
            for i in range(len(g)):
                if g[i] + v <= limit:
                    g[i] += v 
                    if backtrace(arr,g,limit):
                        return True
                    g[i] -= v

                    if g[i] == 0:
                        break 
            arr.append(v)
        def check(limit):
            arr = sorted(jobs)
            groups = [0 for _ in range(k)]
            if backtrace(arr,groups,limit):
                return True
            else:
                return False 
        
        l,r = max(jobs), sum(jobs)
        while l <= r:
            m = (l+r) // 2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l 