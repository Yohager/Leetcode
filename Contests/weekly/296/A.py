class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        arr = []
        for i in range(len(nums) // 2):
            if i % 2 == 0:
                arr.append(min(nums[2*i],nums[2*i+1]))
            else:
                arr.append(max(nums[2*i],nums[2*i+1]))
        # print(arr)
        return self.minMaxGame(arr)