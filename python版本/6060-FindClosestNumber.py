class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dist = []
        n = len(nums)
        for i in range(n):
            dist.append([abs(nums[i]),nums[i]])
        dist.sort(key=lambda x:[x[0],-x[1]])
        # print(dist)
        return dist[0][1]
        
        