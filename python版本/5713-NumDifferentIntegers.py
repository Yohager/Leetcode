class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        tmp = []
        for i in word:
            if i.isdigit():
                tmp.append(i)
            else:
                tmp.append('#')
        print(tmp)
        a = ''.join(tmp)
        a = a.split('#')
        print(a)
        #cnt = 0
        b = []
        for k in a:
            if k:
                b.append(int(k))
        return len(set(b))