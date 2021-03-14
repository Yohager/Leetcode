class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        diff = lambda x,y : (x+1)/(y+1) - x/y
        tmp = []
        ans = 0
        for x,y in classes:
            ans += x/y
            tmp.append((-diff(x,y),x,y))
        
        #将list在线性时间内转换为优先队列
        heapq.heapify(tmp)
        for _ in range(extraStudents):
            d,x,y = heapq.heappop(tmp)
            ans += -d 
            heapq.heappush(tmp,(-diff(x+1,y+1),x+1,y+1))
        return ans / len(classes)