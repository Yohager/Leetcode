class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        min_idx,max_idx = -1,-1
        n = len(nums)
        min_val,max_val = float('inf'),-float('inf')
        for i in range(n):
            if nums[i] < min_val:
                min_val = nums[i]
                min_idx = i 
            if nums[i] > max_val:
                max_val = nums[i]
                max_idx = i 
        #print(min_val,max_val,min_idx,max_idx)
        '''
        三种删除的方式
        '''
        l = min(min_idx,max_idx)
        r = max(min_idx,max_idx)
        #print(r+1,(l+1+n-r),(n-l))
        return min(r+1,(l+1+n-r),(n-l))