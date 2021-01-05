class Solution:
    def countPairs(self, deliciousness) -> int:
        MOD = 1e9+7
        ans = 0
        nums = {}
        for i in deliciousness:
            if i in nums:
                nums[i] += 1
            else:
                nums[i] = 1
        for j in list(nums.keys()):
            for k in range(22):
                if (1<<k) - j in nums and (1<<k) - j != j:
                    ans += nums[j] * nums[(1<<k)-j]
                if (1<<k) == j:
                    ans += nums[j] * (nums[j]-1)
        ans = ans // 2
        return ans % int(MOD)
            

d = [1,1,1,3,3,3,7]

print(Solution.countPairs(Solution,d))