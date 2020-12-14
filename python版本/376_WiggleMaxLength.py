class Solution:
    def wiggleMaxLength1(self, nums: List[int]) -> int:
        #考虑特殊情形
        if len(nums) < 2:
            return len(nums)
        up = 1
        down = 1
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                up = down + 1
            elif nums[i] > nums[i-1]:
                down = up + 1
        return max(up,down)
    
        