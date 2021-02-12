class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:                
        nums = [a,b,c]
        nums.sort()
        if nums[0] == nums[2]-nums[1]:
            return nums[2]
        elif nums[0] < nums[2] - nums[1]:
            return nums[0] + nums[1]
        else:
            dist = nums[2] - nums[1]
            nums[0] -= dist
            nums[2] -= dist
            #现在nums[1]和nums[2]是相等的
            if sum(nums) % 2 == 0:
                #因为后两个数相等，那么如果求和为偶数则第一个数一定是偶数
                k = nums[0] // 2
                return dist + nums[0] + nums[1]-k
            else:
                k = (nums[0] - 1) // 2
                return dist + nums[0]-1 + nums[1]-k