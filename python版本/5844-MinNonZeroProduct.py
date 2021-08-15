class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        '''
        # rounds = 2**(p-1)-1
        # num_round = 2**p - 2 
        #print(rounds,num_round)
        #ans1 = num_round**(rounds) * (2**p-1)
        '''
        if p == 1:
            return 1
        if p == 2:
            return 6
        MOD = 1000000007
        def myPow(x, n):
            res = 1
            x %= MOD
            while n:
                if n & 1:
                    res = res * x % MOD
                x = x * x % MOD
                n >>= 1
            return res % MOD
        r = 2**(p-1) - 1
        #r = r % MOD
        ans = myPow(2*r,r+1) + myPow(2*r,r)
        return ans % MOD