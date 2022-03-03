class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        arr1 = num1[:-1].split('+')
        arr2 = num2[:-1].split('+')  
        a,b = int(arr1[0]), int(arr1[1])
        # print(arr2[1][:-1])
        c,d = int(arr2[0]), int(arr2[1])
        part1 = a*c - b*d 
        part2 = a*d + b*c 
        return str(part1) + '+' + str(part2) + 'i'