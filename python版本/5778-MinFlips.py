class Solution:
    def minFlips(self, s: str) -> int:
#         #分两种情况讨论，可以计算异或值
#         #这个题目本质上就是求有限次操作一的情况下如何才能够使得dist最小
#         ans = float('inf')
#         test = float('inf')
#         n = len(s)
#         #print(n)
#         t = len(s) // 2
#         #print(t)
#         tmp1 = ''
#         tmp2 = ''
#         if n % 2 == 0:
#             #偶数直接怼上去
#             tmp1 += '10'*t 
#             tmp2 += '01'*t 
#         else:
#             #奇数最后加一个
#             tmp1 += '10'*t
#             tmp1 += '1'
#             tmp2 += '01'*t 
#             tmp2 += '0'
#         #构造完成两种情况
#         #print(len(tmp1),len(tmp2))
#         def func(arr):
#             e = arr[0]
#             return arr[1:] + e
#         r1,r2 = 0,0
#         for i in range(n+1):
#             #print(s)
#             p = int(s,2)
#             q = int(tmp1,2)
#             r = int(tmp2,2)
#             c1 = str(bin(p^q))
#             c2 = str(bin(p^r))
#             #r1 = c1.count('1')
#             #r2 = c2.count('1')
#             x1 = sum(list(map(int,list(bin(p^q)[2:]))))
#             x2 = sum(list(map(int,list(bin(p^r)[2:]))))
#             #ans = min(ans,r1,r2)
#             test = min(test,x1,x2)
#             s = func(s)
#         #ans = min(ans,r1,r2)
#         #print(ans,test)
#         return test
#上面的是超时的做法
        # n = len(s)
        # if n % 2 == 0:
        #     b0 = 0
        #     for i in range(n):
        #         if i % 2 == 0:
        #             if s[i] == '1':
        #                 b0 += 1
        #         else:
        #             if s[i] == '0':
        #                 b0 += 1
        #     return min(b0,n-b0)
        
        # b0, b1 = 0,0
        # e0, e1 = 0,0
        # for j in range(n-1,-1,-1):
        #     if j % 2 == 0:
        #         if s[j] == '1':
        #             e0 += 1
        #     else:
        #         if s[j] == '0':
        #             e0 += 1
            
        #     e1 = n - e0
        # ans = min(e0,e1)

        # for k in range(n):
        #     if k % 2 == 0:
        #         if s[k] == '1':
        #             b0 += 1
        #     else:
        #         if s[k] == '0':
        #             b0 += 1
        #     b1 = k + 1 - b0
        #     if k % 2 == 0:
        #         if s[k] == '1':
        #             e0 -= 1
        #     else:
        #         if s[k] == '0':
        #             e0 -= 1
        #     e1 = n - k - 1 - e0 
        
        #     ans = min(ans, b0 + e1)
        #     ans = min(ans, b1 + e0)
        # return ans
        #给出滑动窗口的做法
        n = len(s)
        #这种循环的形式可以弄成两个叠加到一起
        t = s + s 
        a = '01' * n
        b = '10' * n 
        ans = n
        da, db = 0,0
        for i in range(n*2):
            if t[i] != a[i]:
                da += 1
            if t[i] != b[i]:
                db += 1
            if i >= n:
                if t[i-n] != a[i-n]:
                    da -= 1
                if t[i-n] != b[i-n]:
                    db -= 1 
            if i >= n-1:
                ans = min(ans, da, db)
        return ans