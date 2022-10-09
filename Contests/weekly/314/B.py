class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]
        n = len(pref)
        for i in range(1,n):
            res.append(pref[i]^pref[i-1])
        return res 