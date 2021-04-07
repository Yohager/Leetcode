class Solution:
    def searchRange(self, nums, target):
        lb = self.leftbound(nums,target)
        rb = self.rightbound(nums,target)
        if lb == rb:
            return [-1,-1]
        else:
            return [lb,rb-1]
    
    def leftbound(self,nums,target):
        l,r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m+1
            else:
                r = m 
        return l 
    
    def rightbound(self,nums,target):
        l,r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m+1
            else:
                r = m
        return l 


if __name__ == "__main__":
    test = Solution
    nums = [5,7,7,8,8,10]
    target = 6
    print(test.searchRange(test,nums,target))