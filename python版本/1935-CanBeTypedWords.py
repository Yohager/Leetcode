class Solution:
    def canBeTypedWords(self, text: str, broken: str) -> int:
        arr = list(text.split(' '))
        n = len(arr)
        tmp = [1] * n
        cnt = 0
        for idx,t in enumerate(arr):
            for x in broken:
                if x in t:
                    tmp[idx] = 0
        return sum(tmp)