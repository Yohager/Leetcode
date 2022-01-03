class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort() 
        low1 = nums[0]
        for i in range(1,n//2+1):
            #假设nums[i]是high中的最大值 
            cur_k = (nums[i] - low1) // 2 
            if (nums[i]-low1) % 2 or cur_k == 0:
                continue 
            ans = []
            tmp = collections.Counter()
            for j in range(n):
                if tmp[nums[j]-cur_k] > 0:
                    tmp[nums[j]-cur_k] -= 1
                    continue 
                ans.append(nums[j]+cur_k)
                tmp[nums[j]+cur_k] += 1 
            if len(ans) == n // 2:
                return ans 
            
        
        