'''
方法一
dfs
递归输入: 两个节点
退出条件: 当前两个节点都不存在(True), 当前有一个节点不存在(False)
递归: r1.val == r2.val and dfs(r1.left,r2.right) and dfs(r2.left,r1.right)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(node1,node2):
            if not node1 and not node2:
                return True 
            if (node1 and not node2) or (not node1 and node2):
                return False 
            if node1.val != node2.val:
                return False 
            return dfs(node1.left,node2.right) and dfs(node1.right,node2.left)
        return dfs(root,root)
    

'''
方法二
层序遍历
判断每一层的结果是否为正序逆序相等
可以每层取出来后判断也可以在遍历过程中check对应位置的值是否相等
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True 
        def check(s):
            l,r =0,len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False 
                l += 1
                r -= 1
            return True
        q = deque([root])
        while q:
            n = len(q)
            tmp = []
            for _ in range(n):
                cur = q.popleft()
                if cur != '#':
                    tmp.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    else:
                        q.append('#')
                    if cur.right:
                        q.append(cur.right)
                    else:
                        q.append('#')
                else:
                    tmp.append('#')
            if not check(tmp):
                return False 
        return True 


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True 
        q = deque([])
        q.append(root.left)
        q.append(root.right)
        while len(q) > 1:
            l = q.popleft()
            r = q.popleft()
            if not l and not r:
                continue 
            elif not l or not r:
                return False 
            else:
                if l.val != r.val:
                    return False 
            q.append(l.left)
            q.append(r.right)
            q.append(l.right)
            q.append(r.left)
        return True 