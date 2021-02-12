class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        if len(set(A)) < K:
            return 0
        
        def func(A,K):
            n = len(A)
            ans = 0
            l,r = 0,0
            tmp = collections.Counter()
            num = 0
            while r < n:
                if tmp[A[r]] == 0:
                    num += 1
                tmp[A[r]] += 1
                while num > K:
                    tmp[A[l]] -= 1
                    if tmp[A[l]] == 0:
                        num -= 1
                    l += 1
                ans += r-l+1
                r += 1
            return ans
        return func(A,K) - func(A,K-1)