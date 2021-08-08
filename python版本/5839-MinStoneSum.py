class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        tmp = [(-1)*i for i in piles]
        import heapq
        #import math
        heapq.heapify(tmp)
        while k > 0:
            #弹出当前的最小值
            cur = heapq.heappop(tmp)
            cur = cur // 2
            heapq.heappush(tmp,cur)
            k -= 1
            #print(tmp)
        return (-1) * sum(tmp)