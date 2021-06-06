class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        tmp = list(set(nums))
        tmp.sort()
        minval = min(tmp)
        cnt = 0
        for x in nums:
            if x == minval:
                continue
            idx = bisect.bisect(tmp,x)
            cnt += idx-1
        return cnt 