# class TrieTree():
#     def __init__(self):
#         self.child = [None for _ in range(26)]
#         self.is_word = False 
#     def insert(self,word):
#         rt = self 
#         for w in word:
#             idx = ord(w) - ord('a')
#             if not rt.child[idx]:
#                 rt.child[idx] = TrieTree()
#             rt = rt.child[idx]
#         rt.is_word = True 
#     def search(self,target):
#         rt = self 
#         if not target:
#             return False 
#         for t in target:
#             idx = ord(t) - ord('a')
#             if idx in rt.child:
#                 rt = rt.child[idx]
#             elif rt.is_word:
#                 return True 
#             else:
#                 return False 
#         return True 


# if __name__ == "__main__":
#     words = ['hello','apple','banana','orange']
#     NewTrie = TrieTree()
#     for w in words:
#         NewTrie.insert(w)
#     print(NewTrie.search('apple'))

words = ['cat','category','true','trace','top']
trie = {}
for w in words:
    t = trie 
    for x in w:
        if x not in t:
            t[x] = {}
        t = t[x]
    t['#'] = '#'
print(trie)

def search(word):
    t = trie 
    for x in word:
        if x in t:
            t = t[x]
        else:
            return False 
    if '#' in t:
        return True 
    else:
        return False 
print(search('tope'))

        

    