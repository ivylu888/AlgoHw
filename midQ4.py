"""""
 class Node:
            self.next = None
            self.data = data

class LinkList:
    def __int__(self):
        self.head = None

"""""

def insert(self, node):
    if self.head is None:
        node.next = self.head #if null -> return itself
        self.head = node

    elif self.head.data >= node.data:
        node.next = self.head
        self.head = node

    else:
        cur = self.head
        while cur.next is not None and cur.next.data < node.data:
            cur = cur.next

        node.next = cur.next
        cur.next = node
