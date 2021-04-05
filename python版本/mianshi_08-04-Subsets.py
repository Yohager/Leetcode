class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans,path = [],[]
        nums.sort()
        self.dfs(ans,nums,0,path)
        return ans 

    
    def dfs(self,res,arr,idx,path):
        res.append(path[:])
        for i in range(idx,len(arr)):
            path.append(arr[i])
            self.dfs(res,arr,i+1,path)
            path.pop()
        