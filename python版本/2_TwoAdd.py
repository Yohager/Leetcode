#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        #先想办法取出这两个数字
        count_l1 = 0
        count_l2 = 0
        number_1 = 0
        number_2 = 0
        while l1:
            number_1 += l1.val * 10**(count_l1)
            count_l1 += 1
            l1 = l1.next
        while l2:
            number_2 += l2.val * 10**(count_l2)
            count_l2 += 1
            l2 = l2.next
        number_3 = number_1 + number_2
        result_list = list(map(int,str(number_3)))
        result_list.reverse()
        #print(result_list)
        return result_list
        '''
        l3 = ListNode(result_list[0])
        for i in result_list[1:]:
            l3.next = ListNode(i)
            l3 = l3.next
        return l3
        '''


        
'''
if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    test = Solution
    test.addTwoNumbers(test,l1,l2)

'''      


