def FastPow(x,n):
    '''
    目标求解 x**n 
    '''
    if x == 0.0:
        return x 
    res = 1 
    if n < 0:
        x = 1/x 
        n = -n 
    while n:
        if n & 1:
            res *= x 
        x *= x 
        n >>= 1
    return res 

def FastPow2(x,n):
    def quickM(k):
        if k == 0:
            return 1.0 
        y = quickM(k // 2)
        return y*y if not k & 1 else y*y*x 
    return quickM(n) if n >= 0 else 1.0/quickM(-n)

if __name__ == "__main__":
    x= 5
    n = 3 
    print(FastPow(x,n))
    print(FastPow2(x,n))