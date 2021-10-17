class Bank:

    def __init__(self, balance: List[int]):
        self.bank_cnt = {}
        idxs = [i for i in range(1,len(balance)+1)]
        for x,y in zip(idxs,balance):
            self.bank_cnt[x] = y


    def transfer(self, a1: int, a2: int, m: int) -> bool:
        if a1 not in self.bank_cnt or a2 not in self.bank_cnt:
            return False
        if self.bank_cnt[a1] >= m:
            self.bank_cnt[a1] -= m
            self.bank_cnt[a2] += m 
            return True 
        else:
            return False 


    def deposit(self, account: int, money: int) -> bool:
        if account not in self.bank_cnt:
            return False
        else:
            self.bank_cnt[account] += money
            return True
        


    def withdraw(self, account: int, money: int) -> bool:
        if account not in self.bank_cnt:
            return False 
        else:
            if self.bank_cnt[account] < money:
                return False 
            else:
                self.bank_cnt[account] -= money
                return True 



# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)