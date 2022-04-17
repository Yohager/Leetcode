class ATM:

    def __init__(self):
        self.d = [0,0,0,0,0]
        self.k = [20,50,100,200,500]
        self.n = 5
        # self.k2 = [500,200,100,50,20]


    def deposit(self, b: List[int]) -> None:
        for i,x in enumerate(b):
            self.d[i] += x 
        
    def withdraw(self, amount: int) -> List[int]:
        val = amount
        idx = 4 
        res = [0,0,0,0,0]
        while amount > 0 and idx >= 0:
            # print(amount)
            cur = amount // self.k[idx] # 尽可能取贵的需要多少个
            if self.d[idx] < cur:
                # 当前的数量不够用了
                res[idx] = self.d[idx] # 全部用完
                amount -= self.d[idx] * self.k[idx]
            else:
                # 够用
                res[idx] = cur 
                amount = amount % self.k[idx]
            idx -= 1
        if amount > 0:
            return [-1]
        s1 = 0
        for i in range(len(res)):
            s1 += res[i]*self.k[i]
        if s1 != val:
            return [-1]
        for i in range(self.n):
            if res[i] > self.d[i]:
                return [-1]
        for i in range(self.n):
            self.d[i] -= res[i]
        return res 
            


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)