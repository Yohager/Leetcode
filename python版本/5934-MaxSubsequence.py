class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = []
        for i, num in enumerate(nums):
            arr.append([i,num])
        arr.sort(key = lambda x:-x[1])

        idxs = [] 
        for j in range(k):
            idxs.append(arr[j][0])
        idxs.sort()
        res = []
        for idx in idxs:
            res.append(nums[idx])
        return res 