class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = collections.defaultdict(set)
        set1 = set()
        for x,y in paths:
            d[x].add(y)
            set1.add(x)
            set1.add(y)
        for elem in set1:
            if not d[elem]:
                return elem 