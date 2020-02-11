class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if nums == []:
            return []
        result_list = []
        for i in range(len(nums)-k+1):
            #print(nums[i:i+k])
            result_list.append(max(nums[i:i+k]))
        return result_list