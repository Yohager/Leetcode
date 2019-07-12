class Solution_Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 0 #这个count是用来记录左子树节点的个数


#首先的核心想法是需要倒序进行构建二叉树
#第二点需要的是每次记录下进入右子树的次数这个次数决定了前面的数据中有多少小于当前的数据
class Solution:
    def countSmaller(self, nums):
        length = len(nums)
        root = None
        result = [0 for _ in range(length)]
        for i in range(length-1,-1,-1):
            root = self.insert_function(self,root,nums[i],result,i)
        return result
    
    def insert_function(self,root,value,result,index):
        if root == None:
            root = Solution_Node(value)
        elif value <= root.value:
            root.count += 1
            root.left = self.insert_function(self,root.left,value,result,index)
        elif value > root.value:
            result[index] += root.count + 1
            root.right = self.insert_function(self,root.right,value,result,index)
        return root

if __name__ == "__main__":
    test =Solution
    list_test = [5,2,6,1]
    result = test.countSmaller(test,list_test)
    print(result)





    




            


