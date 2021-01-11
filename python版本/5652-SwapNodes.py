# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        def length(head):
            length = 0
            while head:
                head = head.next
                length += 1
            return length
        n = length(head)
        if k > n // 2:
            k = n + 1 - k
        ptr1 = ptr2 = head
        tmp = k-1
        f1 = None
        while tmp > 0:
            f1 = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            tmp -= 1
        #此时ptr1指向的位置是第k个元素
        #ptr2是快指针，ptr3是慢指针
        ptr3 = head
        f2 = None
        while ptr2 != None and ptr2.next != None:
            ptr2 = ptr2.next
            f2 = ptr3
            ptr3 = ptr3.next
            
        '''
        此时f1指向的是第k个元素的前一个元素
        f2指向的是倒数第k个元素的前一个元素
        下面交换元素
        ''' 
        #print(ptr1.val,ptr2.val,ptr3.val)
        if ptr1 == ptr3:
            return head
        if f1 == None and ptr1.next == ptr3:
            ptr3.next = ptr1
            ptr1.next = None
            return ptr3
        if f1 == None and ptr1.next != ptr3:
            temp = ptr1.next
            f2.next = ptr1
            ptr1.next = None
            ptr3.next = temp
            return ptr3
        # if f2 == None and ptr3.next == ptr1:
        #     ptr1.next = ptr3
        #     ptr3.next = None
        #     return ptr1
        # if f2 == None and ptr3.next != ptr1:
        #     temp2 = ptr3.next
        #     f1.next = ptr3
        #     ptr3.next = None
        #     ptr1.next = temp2
        #     return ptr1
            
        if ptr1.next == ptr3: 
            tmp3 = ptr3.next
            f1.next = ptr3
            ptr3.next = ptr1
            ptr1.next = tmp3
            return head
        else:
            tmp1 = ptr1.next
            tmp2 = ptr3.next
            f1.next = ptr3
            ptr3.next = tmp1
            f2.next = ptr1
            ptr1.next = tmp2
            return head