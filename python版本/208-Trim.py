class Node():
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for w in word:
            cur = cur.children[w]
        cur.isword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for w in word:
            cur = cur.children.get(w)
            if cur == None:
                return False
        return cur.isword


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for w in prefix:
            cur = cur.children.get(w)
            if cur == None:
                return False 
        return True 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)