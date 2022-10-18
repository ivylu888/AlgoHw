class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(root):
            if not root: return -1
            depth = max(dfs(root.left), dfs(root.right)) + 1
            if depth == len(res):
                res.append([])

            res[depth].append(root.val)
            return depth
        
        dfs(root)
        return res
