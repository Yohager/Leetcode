class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l,r = 0,n-k
        total = sum(cardPoints)
        tmp = sum(cardPoints[l:r])
        ans = total - tmp
        while r < n:
            tmp -= cardPoints[l]
            tmp += cardPoints[r]
            ans = max(ans,total-tmp)
            l += 1
            r += 1
        return ans

                

