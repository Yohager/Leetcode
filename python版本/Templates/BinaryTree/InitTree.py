class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right 
    
    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"
    
    def __str__(self) -> str:
        return str(self.val)
    

def InitBinaryTree(arr):
    n = len(arr)
    if n == 0:
        return None 
    
    def inner(idx):
        if n <= idx or not arr[idx]:
            return None 
        node = TreeNode(arr[idx])
        node.left = inner(2*idx + 1)
        node.right = inner(2*idx + 2)
        return node 
    return inner(0)


if __name__ == "__main__":
    root = InitBinaryTree([1,2,4,None,None,4,5])
