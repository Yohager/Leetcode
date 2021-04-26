class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        minsize = max(nums)
        maxsize = sum(nums)
        l,r = minsize,maxsize
        while l <= r:
            mid = (l+r) // 2
            cnt = 1
            tmp = 0
            for i in nums:
                if tmp + i > mid:
                    cnt += 1
                    tmp = 0
                tmp += i 
            if cnt <= m:
                r = mid - 1
            else:
                l = mid + 1 
        return l