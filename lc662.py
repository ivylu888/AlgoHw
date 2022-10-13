class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append((root, 0))
        res = 0
        
        while q:
            level = []
            for _ in range(len(q)):
                node, idx = q.popleft()
                level.append(idx)

                if node.left:
                    q.append((node.left, 2*idx))
                if node.right:
                    q.append((node.right, 2*idx+1))
                
            res = max(res, max(level)- min(level) + 1)
            
        return res
