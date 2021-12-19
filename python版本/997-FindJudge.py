class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        c1 = defaultdict(set)
        c2 = defaultdict(set)
        for x,y in trust:
            c1[y].add(x)
            c2[x].add(y)
        #print(c1,c2)
        for x in c1:
            # print(len(list(c1[x])),n-1,c2[x])
            if len(c1[x]) == n-1 and len(c2[x]) == 0:
                #print('here')
                return x 
        return -1