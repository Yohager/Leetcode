class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x:(-len(x),x))
        n = len(s)
        #print(dictionary)
        for x in dictionary:
            idx = 0
            for i in range(n):
                if x[idx] == s[i]:
                    idx += 1
                    if idx == len(x):
                        return x 
        return ''
