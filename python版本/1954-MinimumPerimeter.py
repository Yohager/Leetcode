class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        # ss = [2*i for i in range(10000)]
        # l,r = 0,len(ss)-1
        # while l < r:
        #     m = (l+r) // 2
        #     if 8*sum(list(range(ss[m]//2,ss[m]+1)))-6*ss[m] == neededApples:
        #         return ss[m] * 4 
        #     elif 8*sum(list(range(ss[m]//2,ss[m]+1)))-6*ss[m] > neededApples:
        #         r = m 
        #     else:
        #         l = m + 1
        # return ss[l] * 4
        l,r = 1,1e6
        while l < r:
            m = (l+r) // 2
            if 2*m*(m+1)*(2*m+1) == neededApples:
                return int(8*m) 
            elif 2*m*(m+1)*(2*m+1) < neededApples:
                l = m + 1
            else:
                r = m 
        return int(8*l) 
