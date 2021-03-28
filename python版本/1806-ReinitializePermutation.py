class Solution:
    def reinitializePermutation(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 4:
            return 2
        def func(s):
            cnt = 0
            while s != 1:
                s = s // 2
                cnt += 1
            return cnt
        
        def func1(m):
            c = m
            cnt = 0
            while m != 1:
                if m % 2 == 0:
                    m = m // 2
                    cnt += 1
                else:
                    m = c // 2 + (m-1) // 2
                    cnt += 1
            return cnt
            
        
        if n == 0: return 0
        
        k = n & (n-1)
        #print(k)
        if k == 0:
            return func(n)
        else:
            return func1(n)