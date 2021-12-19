class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l = list(s)
        for x in spaces:
            l[x] = " " + l[x]
        #print(l)
        return ''.join(l)
        