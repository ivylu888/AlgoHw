class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def sym(l, r):
            #both null
            if not l and not r: return True

            if l and r:
                if l.val == r.val:
                    return sym(l.right, r.left) and sym(l.left, r.right)
            return False
    
        return sym(root.left, root.right)
        
