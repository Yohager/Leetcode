class Solution:
    def largestInteger(self, num: int) -> int:
        arr = list(map(int,list(str(num))))
        odd_idx = []
        odd_num = []
        even_idx = []
        even_num = []
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                even_num.append(arr[i])
                even_idx.append(i)
            else:
                odd_num.append(arr[i])
                odd_idx.append(i)
        odd_num.sort(reverse=True)
        even_num.sort(reverse=True)
        res = [0] * len(arr)
        for x,y in zip(odd_idx,odd_num):
            res[x] = y
        for x,y in zip(even_idx,even_num):
            res[x] = y
        return int(''.join(list(map(str,res))))