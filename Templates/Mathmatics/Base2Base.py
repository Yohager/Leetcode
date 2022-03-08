'''
十进制转十进制以内
'''
# 递归写法
def Base10ToBaseX(num,x):
    # num表示十进制数，x表示需要转换到的进制
    if num < x:
        return str(num)
    return str(Base10ToBaseX(num//x,x)) + str(Base10ToBaseX(num%x,x))

# 非递归写法
def Base10ToBaseX2(num,x):
    if not num:
        return '0'
    ans = 0
    pos = 1
    while num > 0:
        tmp = num % x
        ans += tmp * pos 
        pos *= 10
        num = num // x 
    return str(ans)

