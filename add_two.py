# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = 0, 0
        i1, i2 = 0, 0
        cont = True 
        while (cont):
            if (l1):
                num1 += l1.val * (10 ** i1)
                i1 += 1
                l1 = l1.next
            if (l2): 
                num2 += l2.val * (10 ** i2)
                i2 += 1
                l2 = l2.next
            if (not l1 and not l2):
                cont = False
        num3 = num1 + num2
        strNum = num3.str()
        strList = list(strNum)
        head = None
        for str1 in strList:
            newNode = ListNode(int(str1))
            head = newNode            
