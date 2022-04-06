class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dic: List[str]):
        self.a = defaultdict(int)
        self.d = defaultdict(str)
        for k,v in zip(keys,values):
            self.d[k] = v 
        for x in dic:
            if not self.encrypt1(x):
                continue 
            else:
                self.a[self.encrypt1(x)] += 1
        # print(self.a)
        # print(self.d)
    def encrypt1(self,w):
        res = ''
        for y in w:
            if y not in self.d:
                return ''
            res += self.d[y]
        return res 
            
    
    def encrypt(self, word1: str) -> str:
        res = ''
        for w in word1:
            res += self.d[w]
        return res 

    def decrypt(self, word2: str) -> int:
        return self.a[word2]
            



# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)