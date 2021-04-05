class Solution:
    def clumsy(self, N: int) -> int:
        nums = [i for i in range(N,0,-1)]
        # left = N % 4
        # cnt = N // 4
        # res = []
        # for i in range(cnt):
        #     res.append(nums[4*i] * nums[4*i+1] // nums[4*i+2] + nums[4*i+3])
        # ans = res[0]
        # print(res)
        # for k in range(1,len(res)):
        #     ans -= res[k]
        # return ans 
        s = ''
        flag = 0
        d = {
            0:'*',
            1:'//',
            2:'+',
            3:'-'
        }
        for i in range(1,N):
            s += str(nums[i-1])
            s += d[flag]
            flag = i % 4
        s += str(nums[-1])
        return eval(s)