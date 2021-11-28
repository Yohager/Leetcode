class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        sa = []
        n = len(nums)
        if n <= 2*k:
            return [-1]*n
        tmp = nums[0]
        sa.append(tmp)
        for i in range(1,n):
            tmp += nums[i]
            sa.append(tmp)
        
        # print(sa)
        ans = []
        for i in range(k,n-k):
            tmp = sa[i+k] - sa[i-k] + nums[i-k]
            #print(tmp)
            ans.append(tmp // (2*k+1))
        return [-1]*k + ans + [-1]*k
            
                