'''
1. 二叉搜索树寻找两个节点的最近的公共祖先
2. 一般二叉树寻找两个节点的最近的公共祖先
'''
def LowestCommonAncestorBST(root,p,q):
    if not root:
        return None 
    if root.val > p.val and root.val > q.val:
        return LowestCommonAncestorBST(root.left,p,q)
    elif root.val < p.val and root.val < q.val:
        return LowestCommonAncestorBST(root.right,p,q)
    else:
        return root 
    
def LowestCommonAncestorTree(root,p,q):
    if not root:
        return None 
    
    # 是当前节点
    if root == p or root == q:
        return root 
    
    left = LowestCommonAncestorTree(root.left,p,q)
    right = LowestCommonAncestorTree(root.right,p,q)

    if left and right:
        return root 
    
    elif left:
        return left 
    
    elif right:
        return right 
    
    return None 