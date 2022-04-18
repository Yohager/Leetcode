def reverseLinkedList(i,j):
    # 从i节点到j节点之间进行翻转
    dummy = None 
    cur = i 
    while cur != j:
        temp = cur.next 
        cur.next = dummy
        dummy = cur 
        cur = temp 
    cur.next = dummy
    return j,i 


'''
link list的就地逆置
'''
class ListNode:
    def __init__(self,val,nex) -> None:
        self.val = val
        self.next = nex 

def ReverseLL(head):
    pre = ListNode(None,None)
    cur = head 
    while cur:
        nex = cur.next 
        cur.next = pre
        pre = cur 
    return pre.next 
