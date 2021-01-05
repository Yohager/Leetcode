'''
手动实现单调队列
同时完成滑动窗口最大值的题目
单调队列会经常用到一些dp问题的优化上
'''
class Dequeue:
    def __init__(self):
        self.dequeue = []
    
    def queue_push(self,val):
        while self.dequeue and val > self.dequeue[-1]:
            self.dequeue.pop(-1)
        self.dequeue.append(val)
    
    def queue_pop(self,val):
        if self.dequeue and val == self.dequeue[0]:
            self.dequeue.pop(0)
    
    def queue_max(self):
        #temp = self.dequeue
        return self.dequeue[0]
    

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums: return 
        myqueue = Dequeue()
        n = len(nums)
        ans = []
        for i in range(n):
            if i < k-1:
                myqueue.queue_push(nums[i])
            else:
                print(i)
                myqueue.queue_push(nums[i])
                ans.append(myqueue.queue_max())
                myqueue.queue_pop(nums[i-k+1])
        return ans


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution.maxSlidingWindow(Solution,nums,k))
    # test = Dequeue()
    # test.queue_push(1)
    # print(test.dequeue)