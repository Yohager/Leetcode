class MapSum:

    def __init__(self):
        self.trie = dict()

    def insert(self, key: str, val: int) -> None:
        node = self.trie
        for k in key:
            if k not in node:
                node[k] = dict()
            node = node[k]
        node["#"] = val

    def sum(self, prefix: str) -> int:
        node = self.trie
        for k in prefix:
            if k not in node:
                return 0
            node = node[k]
        return self.dfs(node)
    
    def dfs(self, node):
        ans = 0
        for k in node:
            if k == '#':
                ans += node[k]
            else:
                ans += self.dfs(node[k])
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
