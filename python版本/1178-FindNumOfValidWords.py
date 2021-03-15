class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        from collections import Counter
        from itertools import combinations
        counter, ans = Counter(filter(lambda x: len(x) <= 7, map(frozenset,words))),[0] * (len(puzzles))
        for idx,p in enumerate(puzzles):
            for c in list(map(lambda i: combinations(p[1:],i),range(7))):
                ans[idx] += sum(counter[frozenset((p[0],)+ele)] for ele in c)
        return ans 
