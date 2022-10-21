class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sum = 0

        def inorder(root):
            if root.val > L and root.left:
                inorder(root.left)
            if root.val >= L and root.val <= R:
                self.sum += root.val
            if root.val < R and root.right:
                inorder(root.right)
        inorder(root)
        return self.sum
