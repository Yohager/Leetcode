class Solution:
    def countSmaller(self, nums):
        if len(nums) == 0: return []
        if len(nums) == 1: return [0]
        #创建一个索引数组用于进行排序
        #原数组nums不进行排序，仅仅用作比较大小的作用
        index = [i for i in range(len(nums))]
        #用于存放最终每一个位置上的smaller的个数
        result = [0 for _ in range(len(nums))]
        self.merge_sort(self,nums,index,result)
        return result


    def merge_sort(self,nums,index,result):
        if len(index) <= 1:
            return index
        mid = len(index) // 2
        left = index[:mid]
        right = index[mid:]
        #递归拆分数组直至全部变为一个元素的list为止
        left = self.merge_sort(self,nums,left,result)
        right = self.merge_sort(self,nums,right,result)
        #print(left)
        #print(right)
        #如果出现了已经构成了有序的数组直接返回
        left_pointer = 0
        right_pointer = 0
        if (nums[left[-1]] < nums[right[0]]):
            return index
        else:
            for i in range(len(index)):
                if left_pointer >= len(left):
                    index[i] = right[right_pointer]
                    #result[index[i]] += len(right)
                    right_pointer += 1
                elif right_pointer >= len(right):
                    index[i] =  left[left_pointer]
                    left_pointer += 1
                    result[index[i]] += len(right)
                elif nums[left[left_pointer]] <= nums[right[right_pointer]]:
                    index[i] = left[left_pointer]
                    left_pointer += 1
                    result[index[i]] += len(right[:right_pointer])
                else:
                    index[i] = right[right_pointer]
                    #print('process is here')
                    right_pointer += 1
                    #result[index[i]] += len(left)
            #print('index_list',index)
            return index
    '''
    def merge(nums,left,right):
        while left and right:
            pass
    '''





        








if __name__ == '__main__':
    test = Solution
    result = test.countSmaller(test,[5,2,6,1])
    print(result)