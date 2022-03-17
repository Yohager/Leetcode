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

