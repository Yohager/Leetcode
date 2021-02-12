class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        res = 0
        n = len(nums)
        if n <= 1: return True
        if nums[0] > nums[1]:
            nums[0] = nums[1]
            res += 1
        for i in range(1,n-1):
            if nums[i] > nums[i+1]:
                res += 1
                if res > 1:
                    return False
                if nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return True