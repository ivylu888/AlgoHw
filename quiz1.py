#1
def rotate(self, nums:list):
  length = len(nums)
  k = k%length
  nums[:] =nums[length - k:] + nums[:length - k]
  return nums

  


#2
def isSameTree(self, root:TreeNode, p: TreeNode, q: TreeNode)-> bool:
  if not root: return True
  if not p or not q or p.val != q.val: 
    return False
  return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))


#level order traversal
def levelOrder(self, root):
  res = []
  q = deque([root])
  
 
  while q:
    level = []
    for _ in range(len(q)):
      node = q.popleft()
      level.append(node.val)
      if node.left: 
        q.append(node.left)
      if node.right:
        q.append(node.right)
    res.append(level)
  reurn res
        
  
  

               
               
    
