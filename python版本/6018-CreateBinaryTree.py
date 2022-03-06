# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self,arr,root,i,n):
        if i < n:
            tmp = TreeNode(arr[i])
            root = tmp 
            root.left = self.construct(arr,root.left,2*i+1,n)
            root.right = self.construct(arr,root.right,2*i+2,n)
        return root
    
    def createBinaryTree(self, des: List[List[int]]) -> Optional[TreeNode]:
        n = len(des) + 1 # 表示当前的树一共有n个节点
        d1 = defaultdict(list)
        d2 = defaultdict(list)
        for x,y,z in des:
            d1[x].append([y,z])
            d2[y].append(x)
        
        rv = list(set(d1.keys())-set(d2.keys()))[0]
        res = []
        vis = set()
        res.append([rv])
        vis.add(rv)
        idx = 0
        while len(vis) != n:
            cur = res[idx]
            tmp = []
            for x in cur:
                if x != None:
                    childs = d1[x]
                    childs.sort(key=lambda x:-x[1])
                    if len(childs) == 0:
                        tmp.append(None)
                        tmp.append(None)
                    elif len(childs) == 1:
                        if childs[0][1] == 0:
                            tmp.append(None)
                            tmp.append(childs[0][0])
                            vis.add(childs[0][0])
                        else:
                            tmp.append(childs[0][0])
                            tmp.append(None)
                            vis.add(childs[0][0])
                    else:
                        tmp.append(childs[0][0])
                        tmp.append(childs[1][0])
                        vis.add(childs[0][0])
                        vis.add(childs[1][0])
            res.append(tmp)
            idx += 1
        # print(res)
        arr = []
        for r in res:
            for e in r:
                arr.append(e)
        # print(arr)
        for i in range(len(arr)-1,-1,-1):
            if arr[i] == None:
                arr.pop(i)
            else:
                break
        return self.construct(arr,None,0,len(arr))
    
            
        
                
                
            
        
        
        
        
        
        
            
                
            
                
            
        
        
        