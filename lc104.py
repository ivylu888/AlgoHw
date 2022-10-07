             ######  recursive DFS  ######
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
       if not root: return 0

       return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



             ######  BFS with queue  ######
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

      
      
       ######  iterative DFS in preorder  ######
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        if not root: 
            return 0
        res = 0

        while stack:
            node, depth = stack.pop() 

            if node:
                res = max(res, depth) #keep updating res
                #無論是不是null（0）都加入stack
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
      
