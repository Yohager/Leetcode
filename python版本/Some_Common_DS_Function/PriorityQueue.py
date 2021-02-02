#-*-coding:utf-8-*-
'''
priorityQueue Function
'''
MAXSIZE = 100
class PriorQueue():
    def __init__(self):
        self.queue = [[i] for i in range(1,MAXSIZE+1)]
        self.counts = 0
    #获取输出队列内容
    def GetQueue(self):
        res = []
        for i in self.queue:
            for k in range(1,len(i)):
                res.append(i[k])
        return res
    #返回队列中的元素个数
    def Counts(self):
        return self.counts
    #判断队列是否为空
    def IsEmpty(self):
        return True if self.counts == 0 else False
    #输入数据入队列
    def push(self,elem):
        if elem[0] not in self.queue[elem[1]]:
            self.queue[elem[1]].append(elem[0])
            self.counts +=1 
        else:
            return 
    #数据出队
    def pop(self):
        for i in self.queue:
            if len(i) > 1:
                i.pop(1)
                break
            else:
                continue


if __name__ == "__main__":
    temp = PriorQueue()
    test = [[40,3],[30,3],[40,1],[10,1],[20,1],[30,2],[40,3]]
    for i in test:
        temp.push(i)
    print(temp.GetQueue())
    temp.pop()
    print(temp.GetQueue())
    
