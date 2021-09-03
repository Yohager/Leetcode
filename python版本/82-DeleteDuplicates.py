# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None 
        ans = []
        temp = head 
        while temp:
            ans.append(temp.val)
            temp = temp.next 
        c = collections.Counter(ans)
        d = []
        for x in c:
            if c[x] == 1:
                d.append(x)
        d.sort()
        if not d:
            return None
        res = ListNode(d[0])
        tmp = res 
        for i in range(1,len(d)):
            newnode = ListNode(d[i])
            tmp.next = newnode
            tmp = tmp.next 
        return res 