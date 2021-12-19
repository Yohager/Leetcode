class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        tmp = [[] for _ in range(k)]
        for i in range(n):
            tmp[i % k].append(arr[i])
        #print(tmp)
        ans = 0
        def lengthOfLIS(nums: List[int]) -> int:
            lentis = []
            for t in nums :
                nt = bisect.bisect(lentis, t+0.1)
                if nt >= len(lentis) :
                    lentis.append(t)
                else :
                    lentis[nt] = t
            # print(lentis)
            return len(lentis)
        
        def deal(arrt) :
            to_ret =  len(arrt) - lengthOfLIS(arrt)
            # print(arrt, to_ret)
            return to_ret
    
        for s in tmp:
            ans += deal(s)
        return ans 