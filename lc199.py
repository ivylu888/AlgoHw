## BFS with Queue ##
#每一層最後一個append（&pop）的就是最右邊的

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        res = []

        while q:
            rightSide = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
        
            if rightSide: 
                res.append(rightSide.val)
        return res
