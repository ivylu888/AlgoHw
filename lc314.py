class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        res = []
        dic = collections.defaultdict(list)
        q = collections.deque()
        q.append((root, 0))


        while q:
            node, col = q.popleft()
            dic[col].append(node.val)
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
        left = min(dic.keys())
        right = max(dic.keys())

        #right is not included 
        for i in range(left, right + 1):
            res.append(dic[i])
        return res
            
#Runtime 30 ms Beats 98.75%
#Memory 13.9 MB Beats 79.95%
