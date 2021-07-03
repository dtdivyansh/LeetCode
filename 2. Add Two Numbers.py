# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        p1 = l1
        p2 = l2
        c = 0
        a1 = ans
        while(p1!=None or p2!=None):
            
            if(p2==None or p1==None):
                v = c + p2.val if(p1==None) else c+p1.val
                if(p1==None):
                    p2 = p2.next
                else:
                    p1 = p1.next
                r = v%10
                c = (v-r)//10
                a1.val = r
                if(p2!=None or p1!=None):
                    a1.next = ListNode()
                    a1 = a1.next
                else:
                    if(c):
                        a1.next = ListNode()
                        a1 = a1.next
                        a1.val = c
            elif(p1!=None and p2!=None):
                v = c + p2.val + p1.val
                p2 = p2.next
                p1 = p1.next
                r = v%10
                c = (v-r)//10
                a1.val = r
                if(p2!=None or p1!=None):
                    a1.next = ListNode()
                    a1 = a1.next
                else:
                    if(c):
                        a1.next = ListNode()
                        a1 = a1.next
                        a1.val = c
            
        return ans
