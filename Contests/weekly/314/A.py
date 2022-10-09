class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        res = []
        cur = 0
        for idx, t in logs:
            res.append([idx, t - cur])
            cur = t 
        # print(res)
        res.sort(key=lambda x:[-x[1], x[0]])
        return res[0][0]