class BTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BTree:
    def __init__(self,root):
        self.root = root
    
    def is_empty(self):
        if self.root == None:
            return None
    '''
    查找指定的值
    '''
    def find_value(self,value):
        if self.root == None:
            return None
        else:
            return self.search(value,self.root)
    #使用递归寻找数值
    def search(self,value,node):
        if node == None:
            return None
        elif node.data == value:
            return node
        elif value < node.data:
            return self.search(value,node.left)
        else:
            return self.search(value,node.right)
    '''
    插入指定的值
    '''
    def insert(self,value):
        #创建值为value的结点
        node = BTNode(value)
        #如果没有根节点则将这个node赋给root
        if self.root == None:
            self.root = node
        else:
            #从根节点开始搜索
            current_node = self.root
            while True:
                #如果当前想要插入的值小于根节点则继续往左子树寻找
                if value <= current_node.data:
                    if current_node.left != None:
                        current_node = current_node.left
                    else:
                        current_node.left = node
                        break 
                elif value > current_node.data:
                    if current_node.right != None:
                        current_node = current_node.right
                    else:
                        current_node.right = node
                        break
                else:
                    break
    '''
    删除指定的结点
    '''
    def delete(self,value):
        delete_node = self.find_value(value)
        if delete_node == None:
            raise ValueError("Sorry, Not value in Tree")
        else:
            #需要删除的是叶子结点则直接删除即可
            if delete_node.left == None and delete_node.right == None:
                delete_node.data = None
            #单分支结点，只需要考虑修改左右子树的位置，这种情况只有右子树
            elif delete_node.left == None:
                delete_node = delete_node.right
            #单分支结点，只需要考虑修改左右子树的位置，这种情况只有左子树
            elif delete_node.right == None:
                delete_node = delete_node.left
            #考虑此时的情况删除节点的左右子树都不为空
            elif delete_node.left != None and delete_node.right != None:
                pre = delete_node.right
                if pre.left == None:
                    #如果待删除节点的右孩子没有左子树，则待删除节点的整个右子树最小值为其右孩子
                    delete_node.data = pre.data
                    delete_node.right = pre.right
                    del pre
                else:
                    next_node = pre.left
                    while next_node.left != None:
                        pre = next_node
                        next_node = next_node.left
                    delete_node.data = next_node.data
                    pre.left = next_node.right
                    del next_node

    
    #二叉树中序遍历
    def print_btree(self,node,result_list):
        if node == None:
            return node
        result_list.append(node.data)
        self.print_btree(node.left,result_list)
        self.print_btree(node.right,result_list)
    
    def print_function(self):
        result_list = []
        self.print_btree(self.root,result_list)
        print(result_list)



if __name__ == "__main__":
    root = BTNode(2)
    btree = BTree(root)
    btree_list = [7,2,4,9,5,1]
    for i in btree_list:
        btree.insert(i)
    btree.print_function()