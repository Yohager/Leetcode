class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        maxv = max(nums)
        d = defaultdict(int)
        for x in nums:
            d[x] += 1
        
        for i in range(1,maxv+1):
            for j in range(2*i,maxv+1,i):
                d[i] += d[j]
        ans = 0
        for y in nums:
            ans += d[k // gcd(y,k)]
        for p in nums:
            if p*p % k == 0:
                ans -= 1
        return ans // 2