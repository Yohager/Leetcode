class Solution:
    def numberOfArrays(self, ds: List[int], l: int, r: int) -> int:
        ds = [0] + ds
        n = len(ds)
        tmp = [ds[0]]
        for i in range(1,n):
            tmp.append(tmp[i-1]+ds[i])
        #print(tmp)
        minv, maxv = min(tmp), max(tmp)
        # lb, rb = -float('inf'), float('inf')
        # for x in range(l,r+1):
        #     if minv + x >= l and maxv+x <= r:
        #         lb = x
        #         break 
        # for y in range(r,l-1,-1):
        #     if minv + y >= l and maxv+y <= r:
        #         rb = y
        #         break
        # print(lb,rb)
        # return rb-lb
        # print(minv,maxv)
        ans = 0
        for x in range(l,r+1):
            if minv + x >= l and maxv+x <= r:
                ans += 1
        return ans 
            