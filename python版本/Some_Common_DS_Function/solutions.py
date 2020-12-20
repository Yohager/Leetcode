'''
给一个字符串，使得剩余的字符可以通过重新排列的方法形成回文串
'''
def solution(s):
    ans = 0
    counter = collections.Counter(s)
    for value in counter.items:
        if value % 2:
            ans += 1
    return max(0,ans-1)

'''
给定一棵二叉树，每个节点包含一个int范围的值
1. 涉及相应的数据结构
2. 判断是不是完全二叉树
3. 判断其是不是二叉搜索树
'''

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def Traversal(root,ans):
    if root == None:
        return None
    ans.append(root.val)
    Traversal(root.left,ans)
    Traversal(root.right,ans)

def SequenceTraversal(root):
    if root == None:
        return []
    queue = [root]
    result = []
    while queue:
        i = queue[0]
        result.append(i.val)
        if i.left:
            queue.append(i.left)
        if i.right:
            queue.append(i.right)
        queue.pop(0)
    return result


def JudgeBinaryCompleteTree(root):
    if root == None:
        return True
    '''
    一共存在四种情况：一个节点存在左右孩子；一个节点左空右不空；一个节点右空左不空；一个节点左右均为空
    第一种情况下：将这两个节点直接加下去继续遍历
    第二种情况下：直接返回false
    第三种情况和第四种情况下需要继续看后面还有没有节点了
    '''
    queue = [root]
    state = False
    while queue:
        temp = queue[0]
        queue.pop(0)
        if (state and (temp.left or temp.right)) or (temp.left == None and temp.right):
            return False
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
        if (temp.left == None and temp.right == None) or (temp.left and temp.right == None):
            state = True 
    return True
            

if __name__ == "__main__":
    TreeNode1 = TreeNode(1,None, None)
    TreeNode2 = TreeNode(2,None, None)
    TreeNode3 = TreeNode(3,None, None)
    TreeNode4 = TreeNode(4,None, None)
    TreeNode5 = TreeNode(5,None, None)
    TreeNode6 = TreeNode(6,None, None)
    TreeNode1.left = TreeNode2
    TreeNode1.right = TreeNode3
    TreeNode2.left = TreeNode4
    TreeNode2.right = TreeNode5
    TreeNode3.left = TreeNode6
    result = []
    Traversal(TreeNode1,result)
    print(result)
    print(SequenceTraversal(TreeNode1))
    print(JudgeBinaryCompleteTree(TreeNode1))
    






