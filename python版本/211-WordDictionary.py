class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}



    def addWord(self, word: str) -> None:
        tmp = self.trie
        for x in word:
            if x not in tmp:
                tmp[x] = {}
            tmp = tmp[x]
        tmp['#'] = {}


    def search(self, word: str) -> bool:
        word += "#"
        bfs = deque([(0, self.trie)])
        while bfs:
            idx, cur = bfs.popleft()
            if idx == len(word):
                return True 
            if word[idx] == '.':
                for nxt in cur.values():
                    #如果当前为. 则所有在字典中的key都可以作为下一个元素
                    bfs.append((idx+1,nxt))
            elif word[idx] in cur:
                bfs.append((idx+1,cur[word[idx]]))
        return False
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)