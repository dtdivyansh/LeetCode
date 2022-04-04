class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dic= {}
        p = head
        c=1
        while(p!=None):
            dic[c] = p
            c+=1
            p = p.next
            
        temp = dic[k].val
        dic[k].val = dic[c-k].val
        dic[c-k].val = temp
        return head
