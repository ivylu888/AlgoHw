class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.prev = None
        self.head = None

        if not root:
            return 
        
        def inOreder(cur):
            if not cur:
                return 
            inOreder(cur.left)

            if not self.prev:
                self.head = cur
            else:
                self.prev.right = cur
                cur.left = self.prev
            
            self.prev = cur
            inOreder(cur.right)
        
        inOreder(root)
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head

