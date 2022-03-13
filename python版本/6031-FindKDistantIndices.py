class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        if not nums:
            return []
        def check(idx,idxs):
            for x in idxs:
                if abs(idx-x) <= k:
                    return True 
            return False 
        n = len(nums)
        keys = []
        ans = []
        for i in range(n):
            if nums[i] == key:
                keys.append(i)
        for j in range(n):
            if check(j,keys):
                ans.append(j)
        return ans 
        