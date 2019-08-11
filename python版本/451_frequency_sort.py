class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        init_list = []
        sort_list = []
        sort_number = []
        for i in set(s):
            init_list.append(i)
            sort_list.append(s.count(i))
        dict_sort_str = dict(zip(init_list,sort_list))
        print(dict_sort_str)
        sort_new_list = sorted(dict_sort_str.items(),key=lambda x:x[1],reverse=True)
        result_str = ''
        for i in range(len(sort_new_list)):
            result_str += sort_new_list[i][0]*sort_new_list[i][1]
        return result_str