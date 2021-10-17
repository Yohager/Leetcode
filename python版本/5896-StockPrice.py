import sortedcontainers
class StockPrice:

    def __init__(self):
        self.dic = sortedcontainers.SortedDict()
        self.values = sortedcontainers.SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.dic:
            self.values[self.dic[timestamp]] -= 1
            if self.values[self.dic[timestamp]] == 0:
                del self.values[self.dic[timestamp]]
            if price not in self.values:
                self.values[price] = 1
            else:
                self.values[price] += 1
        else:
            if price not in self.values:
                self.values[price] = 1 
            else:
                self.values[price] += 1
        self.dic[timestamp] = price 

        


    def current(self) -> int:
        tmp = self.dic.peekitem(-1)
        return tmp[-1]

    def maximum(self) -> int:
        tmp = self.values.peekitem(-1)
        #print(self.values)
        return tmp[0]

    def minimum(self) -> int:
        tmp = self.values.peekitem(0)
        return tmp[0]