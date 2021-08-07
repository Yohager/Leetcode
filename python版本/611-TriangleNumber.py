class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0
        nums.sort()
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                tmp = nums[i] + nums[j]
                #在j-n之间二分查找合适的插入位置
                idx = bisect.bisect_left(nums[j+1:n],tmp)
                #print(idx)
                ans += idx 
        return ans 