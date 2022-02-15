class Bitset:

    def __init__(self, size: int):
        self.size = size 
        self.zeros = set(list(range(self.size)))
        self.ones = set()
        


    def fix(self, idx: int) -> None:
        self.ones.add(idx)
        if idx in self.zeros:
            self.zeros.remove(idx)


    def unfix(self, idx: int) -> None:
        self.zeros.add(idx)
        if idx in self.ones:
            self.ones.remove(idx)

    def flip(self) -> None:
        # self.bits = bin((int(self.bits, 2) ^ (2**(len(self.bits)+1) - 1)))[3:]
        # self.bits = self.bits.replace('1', '2').replace('0', '1').replace('2', '0')
        # self.counter[0], self.counter[1] = self.counter[1], self.counter[0]
        # # print(self.bits)
        self.ones, self.zeros = self.zeros, self.ones 


    def all(self) -> bool:
        return len(self.ones) == self.size


    def one(self) -> bool:
        return len(self.ones) > 0


    def count(self) -> int:
        return len(self.ones)


    def toString(self) -> str:
        tmp = ['0'] * self.size
        for idx in self.ones:
            tmp[idx] = '1'
        return ''.join(tmp)
            

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()