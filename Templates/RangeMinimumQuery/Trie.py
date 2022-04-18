'''
字典树 主要作用是查询
'''


class TreeNode:
    '''
    A node in the trie structure
    '''
    def __init__(self,w) -> None:
        self.w = w # 存储的单词
        self.is_leaf = False # 是否是结尾
        self.counter = 0
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = TreeNode("")
    
    def insert(self,word):
        node = self.root 
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                # 还未添加
                new_node = TreeNode(c)
                node.children[c] = new_node
                node = new_node 
        node.is_leaf = True 
        node.counter += 1
    
    def dfs(self,node,prefix):
        '''
        dfs to traversal the trie tree 
        '''
        if node.is_leaf:
            self.output.append((prefix+node.w,node.counter))
        for child in node.children.values():
            self.dfs(child,prefix+node.w)
    
    def query(self,x):
        self.output = []
        node = self.root 
        # print(node.is_leaf)
        for c in x:
            if c in node.children:
                node = node.children[c]
            else:
                return [] 
        self.dfs(node,x[:-1])
        return sorted(self.output,key=lambda x:x[1],reverse=True)

if __name__ == "__main__":
    t = Trie()
    words = ['was','word','war','what','where','wh']
    for w in words:
        t.insert(w)
    print(t.query('where'))