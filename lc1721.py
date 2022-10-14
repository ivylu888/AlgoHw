class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = head
        #find 前k
        for _ in range(k-1):
            l = l.next
        
        tail = l
        r = head
        while tail.next:
            tail = tail.next
            r = r.next
        r.val, l.val = l.val, r.val 

        return head
        

#本題目標：if k = 2， 意思是 第二個跟倒數第二個node互換
#作法：三個指針，一個第k，一個倒數k，一個定位最尾
#step 1: l、r 指針起始點在head，用l指針存第k位置（走k-1步）
#step 2： r指針存倒數第k位置，原理：abs(l-tail) = abs(r-tail)
#把 tail 設為 l， 此時r = head； l = tail
#tail設置成快指針找尾巴，r 跟 tail同時前進（持續保持距離k）
