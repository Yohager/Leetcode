class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        # print(c)
        for i,n in enumerate(num):
            # print(i,int(n))
            if c[str(i)] != int(n):
                return False 
        return True 