class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman_int = {'I':1,
                          'V':5,
                          'X':10,
                          'L':50,
                          'C':100,
                          'D':500,
                          'M':1000}
        int_result = []
        length = len(s)
        result = 0
        for i in s:
            if i in dict_roman_int.keys():
                int_result.append(dict_roman_int.get(i))
        print(int_result)
        diff_list = []
        for j in range(length-1):
            diff_list.append(int_result[j]-int_result[j+1])
        print(diff_list)
        counter = 0
        for k in diff_list:
            if k >= 0 :
                counter += 1
        #print(counter)
        if counter == length-1:
            #print(sum(int_result))
            return sum(int_result)
        else:
            #index_ture = [i for i,x in enumerate(diff_list) if x >= 0]
            index_false = [i for i,x in enumerate(diff_list) if x < 0]
            print(index_false)
            for m in range(length):
                if m in index_false:
                   result += abs(diff_list[m])
                   int_result[m+1] = 0
                else:
                    result += int_result[m]
            return result