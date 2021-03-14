class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        from collections import Counter
        arr = [x for y in edges for x in y]
        c = Counter(arr)
        print(c)
        a = list(c.most_common(1))
        return a[0][0]