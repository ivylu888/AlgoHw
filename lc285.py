#iterative T:O(n) Space:O(1)
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        ans = None
        while root:
            if root.val > p.val:
               ans = root
               root = root.left
            else:
                root = root.right
        return ans
        
        
        
#recursive  #T:O(n) S:O(n)
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def helper(root, p):
            if not root:
                return 
            
            if root.val > p.val:
                return helper(root.left, p) or root #if not root.left: return node
            else:
                return helper(root.right, p)
            
        return helper(root, p)
        
       
