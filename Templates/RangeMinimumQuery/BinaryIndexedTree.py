'''
树状数组 BinaryIndexedTree 或者说叫 Fenwick Tree
多用于高效计算数列的前缀和或者区间和
O(log n)的时间复杂度得到任意前缀和
支持O(log n)的时间内动态修改单点值
空间复杂度为 O(n)
'''
class BIT:
    def __init__(self,nums) -> None:
        self.bits = [0] + nums
        self.n = len(self.bits)
        for i in range(1,self.n):
            j = i + self.lowbit(i)
            if j < self.n:
                self.bits[j] += self.bits[i]
        print(self.bits)

    def lowbit(self,x):
        return x & (-x)
    
    def add(self,i,delta):
        i += 1
        while i < len(self.bits):
            self.bits[i] += delta 
            i += self.lowbit(i)
        
    def Prefix(self,i):
        i += 1
        total = 0
        while i > 0:
            total += self.bits[i]
            i -= self.lowbit(i)
        return total 
    

if __name__ == "__main__":
    arr = [1,2,3,4]
    bit_1 = BIT(arr)
    bit_1.add(1,3)
    print(bit_1.bits)
