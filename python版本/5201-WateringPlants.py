class Solution:
    def wateringPlants(self, plants: List[int], c: int) -> int:
        n = len(plants)
        cur = c
        idx = 0
        ts = 0
        while idx < n:
            if cur >= plants[idx]:
                #当前身上的水足够灌溉下一个
                cur -= plants[idx]
                ts += 1
                if idx < n-1 and cur < plants[idx+1]:
                    ts += (idx+1)*2
                    cur = c 
            idx += 1
                
        return ts 