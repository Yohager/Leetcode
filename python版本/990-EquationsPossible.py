from collections import defaultdict
class ufs():
    def __init__(self):
        #self.elems = []
        self.fathers = defaultdict(str)
    
    def initialize(self,arr):
        for i in arr:
            #self.elems.append(i)
            self.fathers[i] = i 
    
    def find(self,x):
        if self.fathers[x] == x:
            return x
        else:
            return self.find(self.fathers[x])
    
    def merge(self,x,y):
        self.fathers[self.find(x)] = self.find(y)

class Solution:
    def equationsPossible(self, equations) -> bool:
        v = list()
        for i in equations:
            if i[0] not in v:
                v.append(i[0])
            if i[-1] not in v:
                v.append(i[-1])
        print(v)

        tmp = ufs()
        tmp.initialize(v)
        for k in equations:
            if k[1] == '=':
                tmp.merge(k[0],k[-1])
        for equ in equations:
            if equ[1] == "!":
                if tmp.find(k[0]) == k[-1] or tmp.find(k[-1]) == k[0]:
                    return False
        return True


        
if __name__ == "__main__":
    arr = ["a==b","b!=c","c==a"]
    print(Solution.equationsPossible(Solution,arr))