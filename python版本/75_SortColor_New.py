class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        blue = len(nums) - 1
        curr = 0
        while (curr <= blue):
            if (nums[curr] == 0):
                temp = nums[curr]
                nums[curr] = nums[red]
                nums[red] = temp
                red += 1
                curr += 1
            elif (nums[curr] == 1):
                curr += 1
            else:
                temp_1 = nums[curr]
                nums[curr] = nums[blue]
                nums[blue] = temp_1
            
