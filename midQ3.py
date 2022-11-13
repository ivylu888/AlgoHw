""""
 class Node:
            self.right = None
            self.left = None
            self.data = data
"""

#print in a range [k1....k2], assume k1 is always less than k2
def printRangeOfBST(root, k1, k2):
    if not root:
        return
    if k1 < root.data:
        print(root.left, k1, k2)
    if k1 <= root.data and k2 >= root.data:
        print(root.data, res = '')
    
    printRangeOfBST(root.right, k1, k2)
