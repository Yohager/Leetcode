class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        d = defaultdict(list)
        for i,j in enumerate(arr):
            d[j].append(i)
        ans = [0] * n 
        for e in d:
            tmp = d[e]
            l = len(tmp)
            cur_v = sum(tmp) - tmp[0]*l 
            for i in range(l):
                diff = tmp[i]-tmp[i-1] if i > 0 else 0 
                cur_v += i * diff - (l-i) * diff 
                ans[tmp[i]] = cur_v 
        return ans 