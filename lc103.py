class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q = collections.deque([root])
        res = []

        if root is None:
            return res

        flag = True #left->right
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if flag:
                    level.append(node.val)
                else: level.insert(0, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            flag = not flag #換方向
            res.append(level)
        return res
