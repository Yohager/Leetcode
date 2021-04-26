class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        '''
        问题研究的是：将数组划分为D个连续的子区间，使得子区间的和最小
        '''
        x = 0
        maxsize = sum(weights)
        minsize = max(weights)
        l,r = minsize, maxsize
        while l <= r:
            m = (l + r) // 2
            cnt = 1
            tmp = 0
            for w in weights:
                if w + tmp > m:
                    cnt += 1
                    tmp = 0
                tmp += w
            if cnt <= D:
                r = m - 1
            else:
                l = m + 1
        return l