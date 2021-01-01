class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        #print(sorted(s))
        while True:
            if len(s) == 1 or len(s) == 0:
                break
            s.sort(reverse = True)
            if s[0] > s[1]:
                s[0] = s[0] - s[1]
                s.pop(1)
            elif s[0] == s[1]:
                s.pop(1)
                s.pop(0)  
        
        return 0 if len(s) == 0 else sum(s)
                