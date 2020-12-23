class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr) - 1:
            return max(arr)
        comp1, count = arr[0], 0
        for i in arr[1:]:
            #如果遇到数组中的其他数大于第一个数则将comp1置为i同时计数器+1
            if i > comp1:
                comp1, count = i, 1
            else:
                count += 1
            
            if count == k:
                return comp1
        return comp1
