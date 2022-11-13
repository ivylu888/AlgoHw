def printLeft(self, root):
    if not root or root.left is None:
        return None
    root.right.next = root.left
    if root.next:
        root.left.next = root.next.right
        self.printLeft(root.left)
        self.printLeft(root.left)

    printLeft(root.left)
    printLeft(root.right)
    return root
  
    
  
