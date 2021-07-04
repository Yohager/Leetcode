class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5 
        if n == 2:
            return 20
        MOD = 1000000000 + 7
        def quickmi(a,b):
            ans = 1
            while b:
                if (b & 1):
                    ans = ans * a % MOD 
                a = a * a % MOD
                b >>= 1
            return ans 
        '''
        5 ** (n+1)//2 * 4 ** (n/2)
        '''
        c = (n + 1) // 2
        d = n // 2
        return (quickmi(5,c) * quickmi(4,d)) % MOD  
