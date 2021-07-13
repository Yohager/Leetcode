class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i in range(n):
            h = n - i
            if h <= citations[i]:
                return h 
        return 0