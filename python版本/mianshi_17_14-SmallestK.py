class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        import heapq
        heapq.heapify(arr)
        return heapq.nsmallest(k,arr)