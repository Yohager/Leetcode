class Solution:
    def countEven(self, num: int) -> int:
        cnt = 0
        def check(t):
            tmp = list(map(int,list(str(t))))
            return True if sum(tmp) % 2 == 0 else False
        
        for i in range(1,num+1):
            if check(i):
                cnt += 1
        return cnt 