class Solution:
    def addDigits(self, num: int) -> int:
        length = len(str(num))
        result_num = num
        while len(str(result_num)) != 1:
            temp = 0
            for i in range(len(str(result_num))):
                #print(num // (10**i) % 10)
                temp += result_num // (10**i) % 10
            #print(temp)
            result_num = temp
        return result_num
    def addDigits_method2(self,number):
        while len(str(number)) != 1:
            number = sum(int(i) for i in str(number))
        return number
    #数学题哈哈哈哈
    def addDigits_method3(self,number):
        return 1+(number - 1)%9










if __name__ == '__main__':
    test = Solution
    result = test.addDigits_method3(test,38)
    print(result)