class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        ans = 0
        l,r = 0,0
        q1 = collections.deque()
        q2 = collections.deque()

        while r < n:
            #维护窗口内的最大值和最小值
            while q1 and q1[-1] > nums[r]:
                q1.pop()
            while q2 and q2[-1] < nums[r]:
                q2.pop()
            q1.append(nums[r])
            q2.append(nums[r])

            while q1 and q2 and q2[0]-q1[0] > limit:
                if nums[l] == q1[0]:
                    q1.popleft()
                if nums[l] == q2[0]:
                    q2.popleft()
                l += 1
            ans = max(ans,r-l+1)
            r += 1
        return ans 