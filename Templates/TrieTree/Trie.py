MAXN = int(1e2)

class Trie:
    def __init__(self):
        self.nex = [[0]*26 for _ in range(MAXN)]
        self.cnt = 0
        self.record = [False] * MAXN
    
    def insert(self,s,l):
        '''
        s: 需要插入的字符串
        l: 需要插入的字符串的长度
        '''
        p = 0
        for i in range(l):
            cur = ord(s[i]) - ord('a')
            if self.nex[p][cur] == 0:
                # 表示当前还没有，添加节点
                self.nex[p][cur] = self.cnt 
                self.cnt += 1
            p = self.nex[p][cur]
        self.record[p] = True 
    
    def search(self,s,l):
        p = 0
        for i in range(l):
            cur = ord(s[i]) - ord('a')
            if self.nex[p][cur] == 0:
                return False 
            p = self.nex[p][cur]
        return self.record[p]
    


if __name__ == "__main__":
    trie_test = Trie()
    for x in ['abc','bcd','eee','adt','dfas']:
        trie_test.insert(x,len(x))
    print(trie_test.nex)

    for y in ['adt','abc','dfsf','wqwer','abc','tt']:
        print(trie_test.search(y,len(y)))
    
