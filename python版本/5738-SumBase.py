class Solution:
    def sumBase(self, n: int, k: int) -> int:
        # def f(n, x):
        #     #n为待转换的十进制数，x为机制，取值为2-16
        #     a=[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
        #     b=[]
        #     while True:
        #         s=n // x  # 商
        #         y=n % x  # 余数
        #         b=b+[y]
        #         if s==0:
        #             break
        #         n=s
        #     b.reverse() # 辗转相除法
        #     ans = ''
        #     for i in b:
        #         ans += str(a[i]) 
        #     return ans
        # ans = f(n,k)
        # arr = list(str(ans))
        # total = 0
        # for i in arr:
        #     total += int(i)
        # return total
        ans = 0
        while n > 0:
            ans += n % k
            n //= k
        return ans