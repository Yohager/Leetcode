class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        def simplify(num,f):
            while num % f == 0:
                num = num // f
            return num 
        n1 = simplify(n,2)
        n2 = simplify(n1,3)
        n3 = simplify(n2,5)
        #print(n1,n2,n3)
        return True if n3 == 1 else False
