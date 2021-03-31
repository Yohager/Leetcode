class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans,path = [],[]
        nums.sort()
        self.dfs(nums,0,ans,path)
        return ans

    
    def dfs(self,nums,idx,ans,path):
        ans.append(path[:])
        for i in range(idx,len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.dfs(nums,i+1,ans,path)
            path.pop()