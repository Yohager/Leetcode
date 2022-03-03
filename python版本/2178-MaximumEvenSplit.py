class Solution:
    def maximumEvenSplit(self, f: int) -> List[int]:
        if f % 2 != 0:
            return []
        t = f // 2
        # 一共可以分解为t个2，贪心从小到大来
        l,r = 0,1000000000
        target = -1
        while l < r:
            m = (l+r) // 2
            if m*(m+1) == 2*t:
                target = m 
                break 
            elif m*(m+1) > 2*t:
                # 找大了
                r = m
            else:
                l = m + 1
        if target == -1:
            target = l - 1
        #print(target)
        if target * (target + 1) == 2 * t:
            return [2*i for i in range(1,target+1)]
        else:
            diff = t - (target * (target+1)//2) # 多出来的值
            ans = [2*i for i in range(1,target+1)]
            ans[-1] += (2*diff)
            return ans 
            