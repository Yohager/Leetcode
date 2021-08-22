class Solution:
    def minTimeToType(self, word: str) -> int:
        if len(word) == 1:
            if word[0] == 'a':
                return 1
            else:
                return 2
        ans = len(word)
        n = len(word)
        ans += min(ord(word[0])-ord("a"),26-(ord(word[0])-ord("a")))
        for i in range(n-1):
            if ord(word[i+1]) <= ord(word[i]):
                ans += min(ord(word[i])-ord(word[i+1]),(26+ord(word[i+1])-ord(word[i])))
            else:
                ans += min(ord(word[i+1])-ord(word[i]),(26+ord(word[i])-ord(word[i+1])))
            #print(ans)
        #ans += min(abs(ord(word[-1])-ord(word[-2])),(26+ord(word[-2])-ord(word[-1])))
        # if word[0] == 'a':
        #     return ans - 1
        # else:
        #     return ans 
        return ans 
