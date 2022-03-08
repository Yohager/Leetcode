'''
思考给定一个带null的数组
将该数组恢复为一棵二叉树
'''
from InitTree import TreeNode

def traversal(root):
    if not root:
        return 
    print(root.val)
    traversal(root.left)
    traversal(root.right)

def reconstruction(arr):
    n = len(arr)
    if not arr:
        return None 
    def construct(node,i):
        if i < n:
            v = TreeNode(arr[i])
            node = v 
            node.left = construct(node.left,2*i+1)
            node.right = construct(node.right,2*i+2)
        return node
    ans = construct(None,0)
    traversal(ans)


if __name__ == "__main__":
    nums = [1,2,2,3,None,None,3,4,None,None,4]
    reconstruction(nums)