class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        d = {num:i for i,num in enumerate(target)}
        #先构建target数组下的字典
        s = []
        for x in arr:
            if x in d:
                tmp = d[x]
                if not s or tmp > s[-1]:
                    s.append(tmp)
                idx = bisect.bisect_left(s,tmp)
                s[idx] = tmp 
        return len(target) - len(s)