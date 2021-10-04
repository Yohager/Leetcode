class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # arr = list(zip(capital,profits))
        # arr.sort(key=lambda x:x[0],-x[1])
        # print(arr)
        # while k > 0:
        #arr = list(zip(capital,profits))
        # d1 = collections.defaultdict(list)
        # for x,y in zip(capital,profits):
        #     # heapq.heapify(d1[x])
        #     # heapq.heappush(d1[x],-y)
        #     d1[x].append(-y)
        # q = []
        # heapq.heapify(q)
        # for item in d1:
        #     if item <= w:
        #         #heapq.heappush(q,heapq.heappop(d1[item]))
        #         for num in d1[item]:
        #             heapq.heappush(q,num)
        #         d1[item] = list()
        # if not q:
        #     return w
        # while k > 0:
        #     if not q:
        #         break
        #     tmp = heapq.heappop(q)
        #     w -= tmp #将当前最大的值取出来完成这个任务
        #     for elem in d1:
        #         if elem <= w:
        #             # if d1[elem]:
        #             #     heapq.heappush(q,heapq.heappop(d1[elem]))
        #             for num in d1[elem]:
        #                 heapq.heappush(q,num)
        #             d1[elem] = list()
        #     k -= 1
        # return w 
        n = len(profits)
        arr = sorted(zip(profits,capital),key=lambda x:x[1])
        q = []
        heapq.heapify(q)
        idx = 0
        while k > 0:
            while idx < n and arr[idx][1] <= w:
                heapq.heappush(q,-arr[idx][0])
                idx += 1
            if q:
                w -= heapq.heappop(q)
            else:
                break 
            k -= 1
        return w 


