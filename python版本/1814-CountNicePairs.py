class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(q):
            return int(str(q)[::-1])
        n = len(nums)
        cnt = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]):
        #             print(nums[i],nums[j])
        #             cnt +=1 
        # print(cnt)
        d = collections.defaultdict(int)
        
        for i in nums:
            cnt += d[i-rev(i)]
            d[i-rev(i)] += 1
             
        return cnt % 1000000007