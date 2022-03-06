from logging import RootLogger
from posixpath import curdir
from InitTree import InitBinaryTree 
from collections import * 

'''
2022.02.23
Traversal.py实现的内容包括:
1. 先/中/后/层序遍历的递归与非递归实现
2. 二叉树深度递归与非递归计算
3. 二叉树叶子节点递归与非递归计算
'''


class BinaryTreeTraversal:
    def __init__(self,nums):
        self.nums = nums
        self.tree = None 
    
    def CreateTree(self):
        self.tree = InitBinaryTree(self.nums)
    
    '''
    求解二叉树深度的递归与非递归写法
    '''
    # 递归写法
    def Depth(self,root):
        if not root:
            return 0 
        return max(self.Depth(root.left),self.Depth(root.right)) + 1

    # 非递归写法
    def NRDepth(self,root):
        if not root:
            return 0 
        q = deque([root])
        depth = 0
        while q:
            depth += 1
            n = len(q)
            cnt = 0
            while cnt < n:
                cnt += 1
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return depth

    '''
    二叉树遍历 递归与非递归的写法
    '''
    
    # 递归的先序/中序/后序遍历
    def PreOrder(self,root):
        if not root:
            return 
        print(root.val)
        self.PreOrder(root.left)
        self.PreOrder(root.right)
    
    def MidOrder(self,root):
        if not root:
            return 
        self.MidOrder(root.left)
        print(root.val)
        self.MidOrder(root.right)

    def PostOrder(self,root):
        if not root:
            return 
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.val)
    
    
    def LevelOrder(self,root):
        if not root:
            return 
        depth = self.Depth(root)
        def func(node,depth):
            if not node or depth == 0:
                print(None)
                return 
            if depth == 1:
                print(node.val)
                return 
            func(node.left,depth-1)
            func(node.right,depth-1)
        
        for i in range(1,depth+1):
            func(root,i)

    # 非递归实现二叉树的四种遍历
    def NRPreOrder(self,root):
        if not root:
            return [] 
        res = []
        stack = []
        cur = root 
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left 
            if stack:
                cur = stack.pop()
                # res.append(cur.val)
                cur = cur.right 
        # print(res)
        return res 
    
    def NRMidOrder(self,root):
        if not root:
            return []
        res = []
        stack = []
        cur = root 
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left 
            if stack:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res 


    # 非递归的后序遍历复杂一些
    def NRPostOrder(self,root):
        if not root:
            return []
        res = []
        stack = []
        cur = root
        vis = {}
        while stack or cur:
            while cur:
                pre = cur 
                vis[cur] = True 
                stack.append(cur)
                cur = cur.left
                
            if stack:
                temp = stack.pop()
                if temp in vis and vis[temp] == True:
                    # 第一次出现在栈顶
                    vis[temp] = False 
                    stack.append(temp)
                    cur = temp.right  
                else:
                    res.append(temp.val)
                    cur = None  
        return res 

    '''
    另一种实现非递归的后序遍历的思路
    考虑所有的根节点都是左右节点访问过后再访问的
    如果当前节点不存在左右节点或者访问过了左右节点则可以访问当前的节点
    如果不是上述的两种情况我们将当前节点的右节点和左节点分别入栈
    每次访问都是访问当前的栈顶元素
    '''
    def NRPostOrder2(self,root):
        if not root:
            return []
        stack = [root]
        res = []
        vis = defaultdict(int)
        # vis[root] = 1
        while stack:
            cur = stack[-1] # 如果当前的栈顶元素没有左右节点则可以直接访问
            if (not cur.left and not cur.right) or vis[cur.left] or vis[cur.right]:
                res.append(cur.val)
                stack.pop()
                vis[cur] = 1
            else:
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        return res 

        
    def NRLevelOrder(self,root):
        '''
        用堆实现层序遍历
        '''
        q = deque([root])
        res = []
        while q:
            cur = q.popleft()
            if cur == '*':
                res.append(None)
            else:
                res.append(cur.val)
                if not cur.left and not cur.right:
                    continue
                if cur.left:
                    q.append(cur.left)
                else:
                    q.append('*')
                if cur.right:
                    q.append(cur.right)
                else:
                    q.append('*')
        return res 
    

    '''
    求tree上的叶子结点的数量
    递归与非递归的求解方式
    '''
    def CntLeaves(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1 
        return self.CntLeaves(root.left) + self.CntLeaves(root.right)

    def NRCntLeaves(self,root):
        if not root:
            return 0 
        q = deque([root])
        res = 0
        while q:
            cur = q.popleft()
            if not cur.left and not cur.right:
                res += 1
            else:
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return res 

    


if __name__ == "__main__":
    # arr = [1,2,3,None,4,None,5]
    arr = [1, 2, None, None, 3, 4, None]
    BTT = BinaryTreeTraversal(arr)
    BTT.CreateTree() 
    # BTT.PreOrder(BTT.tree)
    print('--------')
    # BTT.MidOrder(BTT.tree)
    # print('--------')
    # BTT.PostOrder(BTT.tree)
    # print('--------')
    # # print(BTT.Depth(BTT.tree))
    # # print(BTT.NRDepth(BTT.tree))
    # BTT.LevelOrder(BTT.tree)
    print(BTT.tree)
    print(BTT.NRPreOrder(BTT.tree))
    print(BTT.NRMidOrder(BTT.tree))
    print(BTT.NRPostOrder2(BTT.tree))
    print(BTT.CntLeaves(BTT.tree))
    print(BTT.NRCntLeaves(BTT.tree))