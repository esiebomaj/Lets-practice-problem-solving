# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = dummy = ListNode()
        carry = 0
        while l1 and l2:
            resVal = l1.val + l2.val + carry
            if resVal > 9:
                carry = resVal//10
                resVal = resVal%10
            else:
                carry = 0
            newNode = ListNode(resVal)
            res.next = newNode
            res = res.next
            l1=l1.next
            l2=l2.next
        
        while l1:
            resVal = l1.val + carry
            
            if resVal > 9:
                carry = resVal//10
                resVal = resVal%10
            else:
                carry = 0
            newNode = ListNode(resVal)
            res.next = newNode
            res = res.next
            l1=l1.next
            
        while l2:
            
            resVal = l2.val + carry
            
            if resVal > 9:
                carry = resVal//10
                resVal = resVal%10
            else:
                carry = 0
            newNode = ListNode(resVal)
            res.next = newNode
            res = res.next
            l2=l2.next
        if carry > 0:
            res.next = ListNode(carry)
        return dummy.next
            
            
            
                
        