class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
            while len(ans) >= 2 and gcd(ans[-1],ans[-2]) > 1:
                cur = ans.pop()
                ans[-1] = lcm(cur,ans[-1])
        return ans 