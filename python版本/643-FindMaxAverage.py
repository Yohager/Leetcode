class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sum1 = sum(nums[:k])
        tmpsum = sum1
        ans = tmpsum / k
        for i in range(k,n):
            sum1 -= nums[i-k]
            sum1 += nums[i]
            if sum1 > tmpsum:
                tmpsum = sum1
                ans = tmpsum / k 
        return ans