#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#
class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        if mapping.get(num) != None:
            return mapping.get(num)
        nums_list = list(map(int,str(num)))
        init_list = list(map(int,str(num)))
        #str_list = [0 for _ in range(len(nums_list))]
        str_list = []
        for i in range(len(nums_list)):
            nums_list[i] = nums_list[i] * 10**(len(nums_list)-i-1)
            #print(nums_list[i])
            if mapping.get(nums_list[i]) != None:
                str_list.append(mapping.get(nums_list[i]))
            else:
                if 1 < init_list[i] < 4:
                    str_list.append(init_list[i] * mapping.get(10**(len(nums_list)-i-1)))
                elif 5 < init_list[i] < 9 :
                    str_list.append(mapping.get(5*10**(len(nums_list)-i-1)) + (init_list[i]-5) * mapping.get(10**(len(nums_list)-i-1)))
                else:
                    pass
        result = ""
        for i in str_list:
            result += i
        return result


'''
if __name__ == "__main__":
    test = Solution
    print(test.intToRoman(test,1024))
'''
