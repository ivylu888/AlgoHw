class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def vaild(node, left, right):
            if not node: return True

            if not (left < node.val and right > node.val): #not satisfied 
                return False

            return (vaild(node.left, left, node.val) and vaild(node.right, node.val, right))
        
        return vaild(root, float("-inf"), float("inf"))
