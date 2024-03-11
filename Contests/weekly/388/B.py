class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        h.sort(reverse = True)
        n = len(h)
        ret = 0
        i = 0
        h.append(-10000)
        d = 1
        while k > 0:
            if h[i] < 0:
                break
            ret += h[i]
            h[i + 1] -= d
            d += 1
            i += 1
            k -= 1
        return ret
            
