class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev, cur = dummy, head

        while cur:
            nxt = cur.next
            
            if cur.val == val:
                prev.next = nxt
            else: 
                prev = cur
           
            cur = nxt
        return dummy.next

