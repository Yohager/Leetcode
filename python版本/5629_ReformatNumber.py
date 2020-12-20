class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ","")
        number = number.replace("-","")
        yushu = len(number) % 3
        #余数可能为0,1,2
        #如果余数为0则直接返回一堆3-的形式
        print(number)
        if len(number) <= 3:
            return number
        result = []
        if yushu == 0:
            for i in range(len(number)):
                result.append(number[i])
                if (i+1)%3 == 0 and i != len(number)-1:
                    result.append('-')
        elif yushu == 1:
            #这种情况下是有4个多的
            for i in range(len(number)-4):
                result.append(number[i])
                if (i+1)%3 == 0:
                    result.append('-')
            result.append(number[-4])
            result.append(number[-3])
            result.append('-')
            result.append(number[-2])
            result.append(number[-1])
        elif yushu == 2:
            for i in range(len(number)-2):
                result.append(number[i])
                if (i+1)%3 == 0:
                    result.append('-')
            result.append(number[-2])
            result.append(number[-1])
        return "".join(result)