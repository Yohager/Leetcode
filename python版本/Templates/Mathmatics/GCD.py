'''
三种实现
递归/非递归
math模块集成函数
'''
import math 

def RecursionGCD(m,n):
    if n == 0:
        return m 
    return RecursionGCD(n,m%n)

def NoRecursionGCD(m,n):
    while n != 0:
        r = m % n 
        m = n
        n = r
    return m 

def MathGCD(m,n):
    return math.gcd(m,n) 

if __name__ == "__main__":
    m,n = 12,45
    print(RecursionGCD(m,n),NoRecursionGCD(m,n),MathGCD(m,n))