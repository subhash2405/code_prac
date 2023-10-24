class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add=ListNode()
        current=add
        carry=0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                a=l1.val
            else:
                a=0
            if l2 is not None:
                b=l2.val
            else:
                b=0
            current_sum=a+b+carry
            carry=(current_sum)//10
            current.next=ListNode((current_sum)%10)
            current=current.next

            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
        if carry>0:
            current.next=ListNode(carry)
        return add.next    
