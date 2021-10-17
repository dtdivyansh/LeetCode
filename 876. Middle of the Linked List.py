def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        c=1
        while(tail!=None and tail.next!=None):
            head = head.next
            tail = tail.next.next
        
        return head
