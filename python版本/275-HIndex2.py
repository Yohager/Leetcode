class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #使用二分法
        '''
        考虑可能出现的情况：这个h指数变化的范围是0-n
        使用二分的搜索
        '''
        n = len(citations)
        ans = 0
        l,r = 0,n-1
        while l <= r:
            m = (l+r) // 2
            if n-m <= citations[m]:
                ans = n - m 
                r = m - 1
            else:
                l = m + 1
        return ans