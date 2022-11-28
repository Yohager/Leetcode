class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = dict()
        d[0] = 1
        flag = False 
        total = 0
        ans = 0
        for i in range(n):
            if nums[i] < k:
                total -= 1
            elif nums[i] > k:
                total += 1
            if nums[i] == k:
                flag = True 
            if flag:
                if total in d.keys():
                    ans += d[total]
                if total-1 in d.keys():
                    ans += d[total-1]
            else:
                d[total] = d.get(total, 0) + 1
        return ans 