class Solution:
    def splitListToParts(self, root, k) -> List[Optional[ListNode]]:
        total_len = 0
        head = root
        #找長度
        while head:
            total_len += 1
            head = head.next
        
        ans = [None for _ in range(k)]
        #l = 每個小組平均長度，r = 有多少小組需要增加長度
        l, r = total_len // k, total_len % k 
        prev, head = None, root
        
        for i in range(k):
            ans[i] = head #每個小組的第一個node
            for j in range(l + (1 if r > 0 else 0)):
                prev, head = head, head.next
            
            if prev: 
                prev.next = None #與前面斷開（分完一組）
            r -= 1
        
        return ans
