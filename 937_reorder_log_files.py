class Solution:
    def reorderLogFiles(self,logs):
        new_logs = []
        sort_index = []
        all_sort_index = []
        sort_logs = []
        for log in logs:
            new_logs.append(log.split(' '))
        for j in new_logs:
            j.remove(j[0])
        sort_number = []
        sort_abc = []
        sort_abc_num = []
        for num in range(len(new_logs)):
            if(new_logs[num][0].isdigit()):
                sort_number.append((new_logs[num],num))
            else:
                sort_abc.append(new_logs[num])
                sort_abc_num.append((new_logs[num],num))
        #print(sort_number)
        #print(sort_abc)
        sort_abc.sort()
        #print(sort_abc)
        for element in sort_abc:
            for index in range(len(sort_abc_num)):
                if(element == sort_abc_num[index][0]):
                    all_sort_index.append(sort_abc_num[index][1])
        for num_ele in sort_number:
            all_sort_index.append(num_ele[1])
        #print(all_sort_index)
        for i in all_sort_index:
            sort_logs.append(logs[i])
        return sort_logs
        