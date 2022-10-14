class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        last = head 
        length = 1
        #get the length
        while last.next:
            last = last.next
            length += 1
        
       
        last.next = head  # 5 -> 1
        cur = head

        for _ in range(length - (k%length)-1): #找到3 
            cur = cur.next 
        
        res = cur.next #4 = newHead
        cur.next = None # 3 -> null

        return res
