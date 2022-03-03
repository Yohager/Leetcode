class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        def check(t):
            l = len(t)
            for i in range(l):
                for j in range(i+1,l):
                    if gcd(t[i],t[j]) != 1:
                        return False 
            return True 
        MOD = int(1e9+7)
        '''
        利用条件 1 <= nums[i] <= 30 
        所有的质数: 2,3,5,7,11,13,17,19,23,29
        可能的乘积有2**10个
        '''
        # base = [2,3,5,7,11,13,17,19,23,29]
        base1 = [2,3,5,6,7,10,11,13,14,15,21,22,26,30]
        base2 = [17,19,23,29]
        c = Counter(nums)
        elems = list(c.keys())
        arr2 = [y for y in elems if y in base1]
        '''
        考虑可能的组成方式为：首先不考虑1, 考虑其他所有的素数的排列组合
        '''
        # print(arr2)
        # print(c[1]) 
        # print(len(arr2))
        ans = 0
        n = len(arr2)
        for i in range(1<<n):
            cur = 1
            tmp = []
            for j in range(n):
                if ((i>>j) & 1):
                    cur *= c[arr2[j]]
                    tmp.append(arr2[j])
            if tmp and check(tmp):
                # print(tmp)
                ans += cur 
                ans %= MOD 
        ta = [e for e in elems if e in base2]
        for e in ta:
            ans = ans + ((ans+1)*c[e])
            ans %= MOD
        if c[1] > 0:
            return (ans * (2**(c[1]))) % MOD 
        else:
            return ans % MOD

        


