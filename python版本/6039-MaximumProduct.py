class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # 贪心
        MOD = int(1e9+7)
        n = len(nums)
        nums.sort()
        idx = 0
        while k > 0:
            r = 0
            while r < n and nums[r] == nums[0]:
                r += 1
            # 此时区间l-r都是最小值
            if r == n:
                # 全部相等
                avg = k // n
                left = k % n 
                for i in range(n):
                    nums[i] += avg 
                    if i < left:
                        nums[i] += 1
                k = 0
                break 
            if k < r:
                for i in range(k):
                    nums[i] += 1
                k = 0
                break 
            diff = nums[r] - nums[r-1] # 最小值和次小值之间的差值
            avg = min(diff,k//r)
            for i in range(r):
                nums[i] += avg 
            k -= avg*r
        # print(nums)
        # print(k)
        # avg = k // n
        # left = k % n 
        res = 1
        for i in range(n):
            # nums[i] += avg 
            # if i < left:
            #     nums[i] += 1
            res *= nums[i]
            res %= MOD
        # print(nums)
        return res % MOD 
        