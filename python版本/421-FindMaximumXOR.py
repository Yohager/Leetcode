class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        MAX_SIZE = 30
        ans = 0
        for j in range(MAX_SIZE,-1,-1):
            tmp = set(i >> j for i in nums)
            ans = ans * 2 + 1
            found = False
            for k in tmp:
                if k ^ ans in tmp:
                    found = True
                    break
            if not found:
                ans -= 1
        return ans 
