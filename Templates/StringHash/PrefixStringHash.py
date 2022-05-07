'''
映射规则
f(s)=sum_{i=1}^l s[i] B^{l-i} (mod M)

对于前缀来说，每个字符串最后多出来一个字符, 就相当于在原编码的值的基础上乘上一个base然后加上新的字符的编码值.
对于后缀来说，每个字符串最前多出来一个字符, 就相当于原编码值加上新的字符的编码值乘以base的i-1次幂.
'''
class StringHash:
    def __init__(self,s) -> None:
        self.M = int(1e9+7)
        self.B = 131
        self.s = s
        self.n = len(self.s)
        self.prefix = [0] * (self.n+1)
        self.mults = [1] * (self.n+1)
        self.suffix = [0] * (self.n+1)

    # def get_hash(self,s):
    #     res = 0
    #     for chr in s:
    #         res = (res * self.B + ord(chr)) %self.M 
    #     return res 

    def prefix_suffix_hash(self):
        for i in range(1,self.n+1):
            self.prefix[i] = (self.prefix[i-1]*self.B + (ord(self.s[i-1])-97)) % self.M
            self.mults[i] = self.mults[i-1] * self.B % self.M 
            self.suffix[i] = (self.suffix[i-1]+(ord(self.s[self.n-i])-97)*self.mults[i-1]) % self.M 

    def substring_hash(self,l,r):
        self.prefix_suffix_hash()
        # 计算子串s[l..r]的hash值
        return self.prefix[r] - self.prefix[l-1] * self.mults[r-l+1]



if __name__ == "__main__":
    s1 = 'abcdefg'
    s2 = 'bcdefga'
    sh1 = StringHash(s1)
    sh2 = StringHash(s2)
    print(sh1.substring_hash(3,7))
    print(sh2.substring_hash(2,6))
