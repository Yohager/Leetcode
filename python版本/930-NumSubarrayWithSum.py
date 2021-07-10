class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum1 = sum(nums)
        if sum1 < goal:
            return 0
        res = 0
        tmp = 0
        d = collections.Counter() 
        for i in range(len(nums)):
            tmp += nums[i]
            if  tmp-goal in d.keys():
                res += d[tmp-goal]
            if tmp == goal:
                res += 1
            d[tmp] += 1
        return res 