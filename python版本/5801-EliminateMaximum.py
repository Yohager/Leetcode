class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # ans = 0
        # tmp = []
        # for x,y in list(zip(dist,speed)):
        #     tmp.append([x,y])
        # import heapq
        # heapq.heapify(tmp)
        # #print(tmp)
        # while tmp:
        #     if tmp[0][0] <= 0:
        #         break
        #         # break
        #     for x in tmp:
        #         x[0] = x[0] - x[1]
        #     heapq.heappop(tmp)
        #     ans += 1 
        # return ans 
        tmp = []
        for x,y in list(zip(dist,speed)):
            if x < y:
                tmp.append(0)
            elif x % y == 0:
                tmp.append(x//y-1)
            else:
                tmp.append(x//y)
        tmp.sort()
        print(tmp)
        ans = 1
        n = len(tmp)
        if n == 1:
            return 1
        req = list(range(n))
        print(req)
        for i in range(n):
            if tmp[i] < req[i]:
                #表示额定的处理时间无法处理最晚的处理时间的任务
                return i
        return n
            