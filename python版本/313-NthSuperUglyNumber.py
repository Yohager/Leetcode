class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq 
        h = [1]
        ans = set()
        ans.add(1)
        heapq.heapify(h)
        for i in range(n):
            tmp = heapq.heappop(h)
            for x in primes:
                if tmp*x not in ans:
                    ans.add(tmp*x)
                    heapq.heappush(h,x*tmp)
        return tmp
