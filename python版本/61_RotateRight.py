class Solution:
    def rotateRight(self, head, k):
        if (k == 0):
            return head
        if (head == None):
            return head
        if (head.next == None):
            return head
        if (head.next.next == None):
            if (k % 2 == 0):
                return head
            else:
                p = head.next
                p.next = head
                head.next = None
                return p
        test = head
        length = 1
        while (test.next != None):
            test = test.next
            length += 1
        temp = head
        number = k % length
        #print(number)
        while (number > 0):
            if (temp.next != None):
                temp = temp.next
            else:
                temp = head
            number -= 1
        #此时的temp指针指向的是旋转后的链表的尾节点
        tail_node = temp
        #print(tail_node.val)
        #此时的result指针指向的位置是旋转后的链表的头结点
        result = tail_node.next
        while (temp.next != None):
            temp = temp.next
        temp.next = head
        tail_node.next = None
        return result
        

        