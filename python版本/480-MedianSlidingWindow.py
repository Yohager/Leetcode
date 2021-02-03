class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        l,r = 0,k
        ans = []
        while r <= n:
            tmp = nums[l:r]
            #print(tmp)
            tmp.sort()
            if k % 2 == 0:
                mid = (tmp[k//2] + tmp[k//2-1]) / 2
                ans.append(mid)
            else:
                mid = tmp[k//2]
                ans.append(mid)
            r += 1
            l += 1
        return ans